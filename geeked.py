from manim import *
import math

class PatriotComputationError(Scene):
    def construct(self):
        # ============================================================
        # BUILD / LAYOUT ONLY (no self.play / self.wait up here)
        # ============================================================

        title = Text("Computation Error", font_size=44)

        # -----------------------------
        # Section 1 objects
        # -----------------------------
        dec = MathTex("0.1_{10}", font_size=56)
        dec.to_corner(UL).shift(DOWN * 0.5)

        arrow1 = Arrow(dec.get_right(), dec.get_right() + RIGHT * 2, buff=0.2)

        bin_rep = MathTex(
            "0.00011001100110011001100\\ldots_{2}",
            font_size=46
        ).next_to(arrow1, RIGHT, buff=0.3)

        repeat_box = SurroundingRectangle(bin_rep[0][8:20], color=YELLOW, buff=0.06)
        repeat_label = Text("repeats forever", font_size=28, color=YELLOW)\
            .next_to(repeat_box, DOWN, buff=0.1)

        truncate_arrow = Arrow(
            bin_rep.get_bottom(),
            bin_rep.get_bottom() + DOWN * 0.9,
            buff=0.1
        )

        fixed24 = MathTex(
            "0.00011001100110011001100_{2}",
            font_size=46
        ).next_to(truncate_arrow, DOWN, buff=0.2)

        fixed_lbl = Text("stored in 24-bit register", font_size=28)\
            .next_to(fixed24, DOWN, buff=0.12)

        eps = MathTex(
            "\\varepsilon = 0.1 - 0.00011001100110011001100_{2}",
            font_size=36,
            color=RED
        ).next_to(fixed_lbl, DOWN, buff=0.25).align_to(dec, LEFT)

        section1 = VGroup(
            dec, arrow1, bin_rep,
            repeat_box, repeat_label,
            truncate_arrow, fixed24, fixed_lbl,
            eps
        )

        # -----------------------------
        # Section 2 objects
        # -----------------------------

        axis = NumberLine(
            x_range=[0, 6, 1],
            length=6,
            include_numbers=True
        ).to_corner(DR).shift(UP * 1.2 + LEFT * 0.3)

        true_dot = Dot(axis.n2p(0), color=GREEN)
        stored_dot = Dot(axis.n2p(0), color=RED)

        true_lbl = Text("true time", font_size=22, color=GREEN)\
            .next_to(true_dot, UP, buff=0.3)
        stored_lbl = Text("stored time", font_size=22, color=RED)\
            .next_to(stored_dot, DOWN, buff=0.5)


        
        drift_text = Text("one tick = 0.1s", font_size=20)\
            .next_to(stored_lbl, DOWN, buff=0.2)



        section2 = VGroup(
             axis,
            true_dot, stored_dot,
            true_lbl, stored_lbl,
             drift_text
        )

        # -----------------------------
        # Section 3 objects
        # -----------------------------
        largeT = MathTex(
            "T \\;\\approx\\; \\text{100 hours of operation}",
            font_size=46
        ).to_edge(RIGHT).shift(UP * 1.5)

        float_conv = MathTex(
            "T\\;\\to\\;\\text{floating point}",
            font_size=46
        ).next_to(largeT, DOWN, buff=0.4)

        ulp = MathTex(
            "\\text{ulp}(T) \\text{ grows with exponent}",
            font_size=40, color=YELLOW
        ).next_to(float_conv, DOWN, buff=0.35)

        zoom_axis = NumberLine(x_range=[0, 1, 0.1], length=5)\
            .next_to(ulp, DOWN, buff=0.6).shift(LEFT * 0.3)

        tick_small = VGroup(*[
            Line(
                zoom_axis.n2p(x),
                zoom_axis.n2p(x) + UP * 0.2,
                stroke_width=2
            )
            for x in [0, 0.1, 0.2, 0.3, 0.4, 0.5]
        ])

        zoom_out_label = Text(
            "as T gets big, spacing between representable floats grows",
            font_size=22
        ).next_to(zoom_axis, DOWN, buff=0.3)

        pos_err = MathTex(
            "\\Delta x \\;=\\; v\\,\\Delta t",
            font_size=48, color=RED
        ).next_to(zoom_out_label, DOWN, buff=0.45)

        section3 = VGroup(
            largeT, float_conv, ulp,
            zoom_axis, tick_small,
            zoom_out_label, pos_err
        )

        # -----------------------------
        # Section 4 objects
        # -----------------------------
        ieee_title = Text(
            "Float precision depends on magnitude",
            font_size=30
        ).to_edge(RIGHT).shift(UP * 1.0)

        ex = MathTex(
            "2^{53} + 1 \\;=\\; 2^{53}",
            font_size=52, color=YELLOW
        ).next_to(ieee_title, DOWN, buff=0.5)

        py = Text(
            "python3 -c 'print(9007199254740992.0 + 1.0)'",
            font_size=22
        ).next_to(ex, DOWN, buff=0.4)



        # ============================================================
        # ANIMATION TIMELINE (all self.play / self.wait down here)
        # ============================================================
        section1.shift(DOWN * 1.5)

        # Title
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # ---- Section 1 animation ----
        self.play(FadeIn(dec))
        self.play(GrowArrow(arrow1), FadeIn(bin_rep))
        self.wait(0.5)

        self.play(Create(repeat_box), FadeIn(repeat_label))
        self.wait(0.6)

        self.play( TransformFromCopy(bin_rep, fixed24))
        self.play(FadeIn(fixed_lbl))
        self.wait(0.6)

        self.play(Write(eps))
        self.wait(0.8)

        self.play(section1.animate.scale(0.5).to_corner(UL).shift(DOWN * 0.7))

        # ---- Section 2 animation ----
        self.play( Create(axis))
        self.play(FadeIn(true_dot), FadeIn(stored_dot), FadeIn(true_lbl), FadeIn(stored_lbl))
        self.wait(0.3)

        self.play( FadeIn(drift_text))
        self.wait(0.3)

        for k in range(1, 6):
            true_pos = 0.1 * k
            stored_pos = 0.1 * k - 0.003 * k  # exaggerated epsilon for visibility
            self.play(
                true_dot.animate.move_to(axis.n2p(true_pos)),
                stored_dot.animate.move_to(axis.n2p(stored_pos)),
                run_time=0.1
            )
        self.play(section2.animate.scale(0.5).to_corner(UR).shift(DOWN * 0.7))

        # ---- Section 3 animation ----
        self.play(Write(largeT))
        self.play(Write(float_conv))
        self.play(Write(ulp))
        self.wait(0.6)

        self.play(Create(zoom_axis), FadeIn(tick_small))
        self.wait(0.4)

        self.play(FadeIn(zoom_out_label))
        self.wait(0.6)

        self.play(
            zoom_axis.animate.stretch(0.5, 0).shift(RIGHT * 0.5),
            tick_small.animate.stretch(0.5, 0).shift(RIGHT * 0.5),
            run_time=1.0
        )
        self.play(
            zoom_axis.animate.stretch(0.5, 0).shift(RIGHT * 0.5),
            tick_small.animate.stretch(0.5, 0).shift(RIGHT * 0.5),
            run_time=1.0
        )
        self.wait(0.4)

        self.play(Write(pos_err))
        self.wait(0.8)

        self.play(FadeOut(section3))

        # ---- Section 4 animation ----
        self.play(FadeIn(ieee_title))
        self.play(Write(ex))
        self.play(FadeIn(py))
        self.wait(1.2)


        self.play(*map(FadeOut, self.mobjects))
