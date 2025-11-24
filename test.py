from manim import *
import math
import numpy as np  # needed for vector math

class MissileFollowCurve(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[0, 13, 1],
            y_range=[0, 6, 1],
            x_length=13,
            y_length=5,
        )

        # Domain of the function
        x_min = 2 * (3.15 - math.sqrt(10))
        x_max = 2 * (3.15 + math.sqrt(10))

        # Function y = 1.4*sqrt(10 - (0.5x - 3.15)^2)
        def f(x):
            inside = 10 - (0.5 * x - 3.15)**2
            inside = max(inside, 0)  # avoid tiny negatives
            return 1.4 * math.sqrt(inside)

        graph = axes.plot(f, x_range=[x_min, x_max], color=BLUE)
        dotted = DashedVMobject(graph, num_dashes=60)

        # -------- Missile VGroup --------
        def make_missile():
            body = Rectangle(
                width=0.8,
                height=0.12,
                fill_color=GRAY,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1.5,
            )
            right = body.get_right()
            nose = Polygon(
                right + RIGHT * 0.15,
                right + UP * 0.06,
                right + DOWN * 0.06,
                fill_color=RED,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1.5,
            )
            fin_top = Polygon(
                LEFT * 0.3,
                LEFT * 0.3 + UP * 0.06,
                LEFT * 0.45 + UP * 0.18,
                fill_color=BLUE,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1,
            )
            fin_bottom = Polygon(
                LEFT * 0.3,
                LEFT * 0.3 + DOWN * 0.06,
                LEFT * 0.45 + DOWN * 0.18,
                fill_color=BLUE,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1,
            )
            missile = VGroup(body, nose, fin_top, fin_bottom)
            missile.scale(0.5)
            return missile

        # -------- Radar --------
        def make_radar():
            base = Rectangle(width=0.4, height=0.1, fill_opacity=1).set_color(GREY)
            pole = Rectangle(width=0.06, height=0.4, fill_opacity=1).set_color(GREY_D)
            pole.next_to(base, UP, buff=0)

            dish = Arc(
                start_angle=-PI/2,
                angle=PI,
                radius=0.25,
            ).set_stroke(WHITE, width=2)
            dish.shift(UP * 0.25 + RIGHT * 0.05)

            antenna = Line(ORIGIN, UP * 0.18).set_stroke(YELLOW, width=2)
            antenna.shift(UP * 0.25 + RIGHT * 0.05)

            radar = VGroup(base, pole, dish, antenna)
            return radar

        radar = make_radar()
        radar_pos = axes.c2p(10, 0)
        radar.move_to(radar_pos)

        t = ValueTracker(0.0)

        def get_state(frac):
            x = x_min + frac * (x_max - x_min)
            y = f(x)

            h = 1e-3
            x1 = max(x_min, x - h)
            x2 = min(x_max, x + h)
            y1 = f(x1)
            y2 = f(x2)

            p1 = axes.c2p(x1, y1)
            p2 = axes.c2p(x2, y2)

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            angle = 0 if (dx == 0 and dy == 0) else math.atan2(dy, dx)

            return x, y, angle

        def make_missile_at_t():
            frac = t.get_value()
            x, y, angle = get_state(frac)
            m = make_missile()
            m.rotate(angle)
            m.move_to(axes.c2p(x, y))
            return m

        missile = always_redraw(make_missile_at_t)

        # -------- Radar cone (two beams + yellow + red bands) --------
        beam_length = 20.0
        cone_half_angle = 0.12

        def make_beams_and_bands():
            frac = t.get_value()
            if frac < 1/6:
                return VGroup()

            eff_frac = min(frac, 2/3)
            x, y, _ = get_state(eff_frac)
            missile_point = axes.c2p(x, y)

            vec = missile_point - radar_pos
            base_angle = math.atan2(vec[1], vec[0])

            dir_left = np.array([math.cos(base_angle - cone_half_angle),
                                 math.sin(base_angle - cone_half_angle), 0])
            dir_right = np.array([math.cos(base_angle + cone_half_angle),
                                  math.sin(base_angle + cone_half_angle), 0])

            end_left = radar_pos + beam_length * dir_left
            end_right = radar_pos + beam_length * dir_right
            beam_left = Line(radar_pos, end_left, color=YELLOW, stroke_width=2)
            beam_right = Line(radar_pos, end_right, color=YELLOW, stroke_width=2)

            d = math.hypot(vec[0], vec[1])

            base_width = min(0.8 * d, beam_length * 0.5)
            size_factor = max(1/3, 1 - eff_frac)
            yellow_width = base_width * size_factor

            y_start_len = max(0, d - yellow_width / 2)
            y_end_len   = min(beam_length, d + yellow_width / 2)

            y_start_left  = radar_pos + y_start_len * dir_left
            y_end_left_g  = radar_pos + y_end_len   * dir_left
            y_start_right = radar_pos + y_start_len * dir_right
            y_end_right_g = radar_pos + y_end_len   * dir_right

            yellow_fill = Polygon(
                y_start_left, y_end_left_g, y_end_right_g, y_start_right,
                fill_color=YELLOW, fill_opacity=0.15, stroke_opacity=0
            )

            if eff_frac <= 1/3:
                divergence = 0.0
            else:
                divergence = (eff_frac - 1/3) * 3.0

            min_factor = 0.6
            center_len_red = d * ((1 - divergence) + divergence * min_factor)
            red_width = yellow_width

            r_start_len = max(0, center_len_red - red_width / 2)
            r_end_len   = min(beam_length, center_len_red + red_width / 2)

            r_start_left  = radar_pos + r_start_len * dir_left
            r_end_left_g  = radar_pos + r_end_len   * dir_left
            r_start_right = radar_pos + r_start_len * dir_right
            r_end_right_g = radar_pos + r_end_len   * dir_right

            red_fill = Polygon(
                r_start_left, r_end_left_g, r_end_right_g, r_start_right,
                fill_color=RED, fill_opacity=0.15, stroke_opacity=0
            )

            return VGroup(yellow_fill, red_fill, beam_left, beam_right)

        beams_and_bands = always_redraw(make_beams_and_bands)

        def make_base():
            bunker = Rectangle(
                width=1.2, height=0.4,
                fill_opacity=1, fill_color=GREY_D,
                stroke_color=WHITE, stroke_width=1.5,
            )
            bunker_round_top = ArcBetweenPoints(
                bunker.get_left() + UP * 0.2,
                bunker.get_right() + UP * 0.2,
                angle=PI/2,
            ).set_stroke(WHITE, width=1.5)
            door = Rectangle(
                width=0.25, height=0.25,
                fill_opacity=1, fill_color=BLACK,
                stroke_color=WHITE, stroke_width=1,
            )
            door.next_to(bunker, DOWN, buff=-0.1)

            pole = Line(ORIGIN, UP * 0.8).set_stroke(WHITE, width=2)
            pole.next_to(bunker, UP, buff=0).shift(RIGHT * 0.4)

            flag = Polygon(
                pole.get_end() + RIGHT * 0.02,
                pole.get_end() + RIGHT * 0.5 + UP * 0.12,
                pole.get_end() + RIGHT * 0.5 + DOWN * 0.12,
                fill_color=RED, fill_opacity=1,
                stroke_color=WHITE, stroke_width=1,
            )

            return VGroup(bunker, bunker_round_top, door, pole, flag)

        base = make_base()
        base_pos = axes.c2p(x_max, 0)
        base.move_to(base_pos)

        # --------- NEW: callout helper -----------

        def make_callout(frac, text_str="ADD TEXT"):
            # missile position at this fraction
            x, y, _ = get_state(frac)
            pos = axes.c2p(x, y)

            label = Text(text_str, font_size=28)
            brace = Text("}", font_size=56).rotate(PI/2)  # 90° anticlockwise

            # stack: label on top, brace underneath
            callout = VGroup(label, brace).arrange(DOWN, buff=0.05)

            # tiny lift for the label relative to brace
            label.shift(UP * 0.05)

            brace.shift(LEFT * 0.5)

            # offset near rocket (tune these if you want)
            callout.move_to(pos + UP * 0.55 + RIGHT * 0.6)

            return callout

        # -----------------------------------------

        # -------- Staging of the scene --------
        self.play(Create(axes))
        self.play(FadeIn(radar))
        self.play(FadeIn(base))
        self.play(Create(dotted))
        self.wait(0.2)

        self.add(beams_and_bands)
        self.play(FadeIn(missile))
        self.wait(0.5)

        # ---- Incremental movements; beams + bands track/freeze as specified ----

        # 0 -> 1/6 : missile moves, NO beam yet
        self.play(t.animate.set_value(1/6), run_time=1.5, rate_func=linear)

        callout1 = make_callout(1/6, "Search action")
        self.play(FadeIn(callout1), run_time=0.4)
        self.wait(10)
        self.play(FadeOut(callout1), run_time=0.4)
        self.wait(0.2)

        # 1/6 -> 1/3 : beam appears and starts tracking (both bands accurate)
        self.play(t.animate.set_value(1/3), run_time=1.5, rate_func=linear)

        callout2 = make_callout(1/3, "Validation action")
        self.play(FadeIn(callout2), run_time=0.4)
        self.wait(10)
        self.play(FadeOut(callout2), run_time=0.4)
        self.wait(0.2)

        # 1/3 -> 2/3 : both bands shrink; red smoothly diverges below yellow
        self.play(t.animate.set_value(2/3), run_time=2.0, rate_func=linear)

        callout3 = make_callout(2/3, "Tracking action (failure)")
        self.play(FadeIn(callout3), run_time=0.4)
        self.wait(10)
        self.play(FadeOut(callout3), run_time=0.4)
        self.wait(0.2)

        # 2/3 -> 1 : missile keeps going, but beams + bands stay frozen
        self.play(t.animate.set_value(1.0), run_time=2.0, rate_func=linear)
        self.remove(missile)
        self.play(FadeOut(base))



