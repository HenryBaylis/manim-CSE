from manim import *

# Optional: 16:9 layout like real slides
config.frame_width = 14.222
config.frame_height = 8.0
blue = "#29ABCA"
orange = "#FF6F00"


class Slide1(Scene):
    def construct(self):
        title = Text("Patriot Missile Disaster", font_size=72, weight=BOLD)
        title.move_to(ORIGIN)
        group3 = Text("Group 3", font_size=50, color=blue)
        group3.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(title, scale=1.05))
        self.play(FadeIn(group3))
        self.wait(5)


class Slide2(Scene):
    def construct(self):
        title = Text("How does the Patriot system work?", font_size=50, weight=BOLD)
        i=ImageMobject("images/2.1.jpg")
        i.scale(1)
        i2=ImageMobject("images/2.2.jpg")
        i.scale(0.8)



        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP), run_time=0.6)
        self.play(FadeIn(i))
        self.play(i.animate.to_edge(LEFT), run_time=0.6)
        self.play(FadeIn(i2))
        self.play(i2.animate.to_edge(RIGHT), run_time=0.6)
        self.wait(2)



class Slide3(Scene):
    def construct(self):
        i=ImageMobject("images/3.7")
        t = Text("Radar set", font_size=50)
        i.scale(0.2)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        self.play(FadeIn(i))
        self.wait(1)


class Slide4(Scene):
    def construct(self):
        t = Text("Engagement station", font_size=50)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        i=ImageMobject("images/3.6")
        i.scale(0.2)
        self.play(FadeIn(i))
        self.wait(1)


class Slide5(Scene):
    def construct(self):
        t = Text("Launcher station", font_size=50)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        i=ImageMobject("images/3.3")
        i.scale(0.4)
        self.play(FadeIn(i))
        self.wait(1)

        self.wait(1)


class Slide6(Scene):
    def construct(self):
        t = Text("Antenna", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        i=ImageMobject("images/3.5")
        i.scale(0.15)
        self.play(FadeIn(i))
        self.wait(1)

        self.wait(1)


class Slide7(Scene):
    def construct(self):
        t = Text("Power Generator", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        i=ImageMobject("images/3.4")
        i.scale(0.15)
        self.play(FadeIn(i))
        self.wait(1)


class Slide9(Scene):
    def construct(self):
        t = Text("Who was at fault?", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)
        i=ImageMobject("images/r")
        i.scale(0.9)
        self.play(i.animate.to_edge(LEFT), run_time=0.6)
        j=ImageMobject("images/logo")
        j.scale(1)
        self.play(j.animate.to_edge(RIGHT), run_time=0.6)
        k=ImageMobject("images/US")
        k.scale(0.6)

        self.play(FadeIn(k))
        self.wait(1)

class Slide8(Scene):
    def construct(self):
        t = Text("Taxonomy", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)

        r  = Text("Reliability",      font_size=30, color=blue)
        a  = Text("Availability",     font_size=30, color=blue)
        s  = Text("Safety",           font_size=30, color=blue)
        m  = Text("Maintainability",  font_size=30, color=blue)

        # Stack them top->bottom with spacing
        items = VGroup(r, a, s, m).arrange(DOWN, buff=0.6)
        items.move_to(ORIGIN)

        # Fade in from top to bottom
        self.play(FadeIn(r, shift=UP*0.5), run_time=0.6)
        self.play(FadeIn(a, shift=UP*0.5), run_time=0.6)
        self.play(FadeIn(s, shift=UP*0.5), run_time=0.6)
        self.play(FadeIn(m, shift=UP*0.5), run_time=0.6)


        self.wait(2)

class Slide10(Scene):
    def construct(self):
        t = Text("Taxonomy - Maintainability", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)

        r  = Tex(r"State of source code was not ideal",      font_size=30, color=blue)
        a  = Tex(r"Six Modifications made to the code during the war",     font_size=30, color=orange)
        s  = Tex(r"Proper testing could not be completed",           font_size=30, color=blue)
        m  = Tex(r"Portable data-collectors were installed late or never",  font_size=30, color=orange)

        # Stack them top->bottom with spacing
        items = VGroup(r, a, s, m).arrange(DOWN, buff=0.6)
        items.move_to(ORIGIN)

        # Fade in from top to bottom
        self.play(FadeIn(r, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(a, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(s, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(m, shift=UP*0.5), run_time=0.6)

        self.wait(2)

class Slide11(Scene):
    def construct(self):
        t = Text("Taxonomy - Reliability", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)

        r  = Tex(r"Weapon Control Computer must accurately produce results to intercept hostile missiles",      font_size=30, color=blue)
        a  = Tex(r"Round-off error made the system less reliable over time",     font_size=30, color=orange)
        s  = Tex(r"Run time of 100 hours",           font_size=30, color=blue)
        m  = Tex(r"Cooperation with Israeli Military could have prevented disaster",  font_size=30, color=orange)

        # Stack them top->bottom with spacing
        items = VGroup(r, a, s, m).arrange(DOWN, buff=0.6)
        items.move_to(ORIGIN)

        # Fade in from top to bottom
        self.play(FadeIn(r, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(a, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(s, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(m, shift=UP*0.5), run_time=0.6)

        self.wait(2)

class Slide12(Scene):
    def construct(self):
        t = Text("Taxonomy - Availability", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)

        r  = Tex(r"System had to be unavailable to fix system instability(restart)",      font_size=30, color=blue)
        a  = Tex(r"Restart took between 60-90s",     font_size=30, color=orange)
        s  = Tex(r"Intolerable: system must be available to intercept missiles",           font_size=30, color=blue)

        # Stack them top->bottom with spacing
        items = VGroup(r, a, s).arrange(DOWN, buff=0.6)
        items.move_to(ORIGIN)

        # Fade in from top to bottom
        self.play(FadeIn(r, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(a, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(s, shift=UP*0.5), run_time=0.6)
        self.wait(2)

        self.wait(2)

class Slide13(Scene):
    def construct(self):
        t = Text("Taxonomy - Safety", font_size=60)
        self.play(FadeIn(t))
        self.play(t.animate.to_edge(UP), run_time=0.6)

        r  = Tex(r"The system is inherently dangerous as it houses explosives",      font_size=30, color=blue)
        a  = Tex(r"Even in a broken state, the system was not a direct danger",     font_size=30, color=orange)
        s  = Tex(r"Will not damage its environment but can't prevent damaging attacks",           font_size=30, color=blue)

        # Stack them top->bottom with spacing
        items = VGroup(r, a, s).arrange(DOWN, buff=0.6)
        items.move_to(ORIGIN)

        # Fade in from top to bottom
        self.play(FadeIn(r, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(a, shift=UP*0.5), run_time=0.6)
        self.wait(2)
        self.play(FadeIn(s, shift=UP*0.5), run_time=0.6)

        self.wait(2)


class SlideReferences(Scene):
    def construct(self):
        t = Text("References", font_size=30)
        self.play(FadeIn(t))
        self.play(t.animate.to_corner(UL).shift(RIGHT*0.5), run_time=0.1)

        ref1 = Tex(
            r"Arnold, D. (2021). \textit{The Patriot Missile Failure}. "
            r"Available at: \texttt{umn.edu/\textasciitilde arnold/disasters/patriot.html} "
            r"(Accessed 7 Nov. 2025).",
            font_size=12,
        )

        ref2 = Tex(
            r"Avizienis, A. \textit{et al.} (2004). "
            r"‘Basic concepts and taxonomy of dependable and secure computing’, "
            r"\textit{IEEE Trans. Dependable and Secure Computing}, 1(1), 11--33. "
            r"Available at: \texttt{doi.org/10.1109/TDSC.2004.2} "
            r"(Accessed 9 Nov. 2025).",
            font_size=12,
        )

        ref3 = Tex(
            r"Barr, M. (n.d.). \textit{Case Study: Lethal Software Defects -- Patriot Missile Failure}. "
            r"Available at: \texttt{barrgroup.com/.../case-study-patriot-missile-defects.pdf} "
            r"(Accessed 7 Nov. 2025).",
            font_size=12,
        )

        ref4 = Tex(
            r"History.redstone.army.mil. (n.d.). \textit{The United States Army | Redstone Arsenal Historical Information}. "
            r"Available at: \texttt{history.redstone.army.mil/miss-patriot.html} "
            r"(Accessed 20 Nov. 2025).",
            font_size=12,
        )

        ref5 = Tex(
            r"NATO OTAN. (n.d.). \textit{Patriot Factsheet}. "
            r"Available at: \texttt{nato.int/.../20121204\_121204-factsheet-patriot-en.pdf} "
            r"(Accessed 11 Nov. 2025).",
            font_size=12,
        )

        ref6 = Tex(
            r"\textit{PATRIOT MISSILE DEFENSE: Software Problem Led to System Failure at Dhahran, Saudi Arabia}. (n.d.). "
            r"Available at: \texttt{gao.gov/assets/imtec-92-26.pdf} "
            r"(Accessed 7 Nov. 2025).",
            font_size=12,
        )

        ref7 = Tex(
            r"Wikipedia. (2020). \textit{MIM-104 Patriot}. "
            r"Available at: \texttt{en.wikipedia.org/wiki/MIM-104\_Patriot} "
            r"(Accessed 20 Nov. 2025).",
            font_size=12,
        )

        ref8 = Tex(
            r"Wikipedia Contributors (2019). \textit{Mikoyan MiG-29}. "
            r"Available at: \texttt{en.wikipedia.org/wiki/Mikoyan\_MiG-29} "
            r"(Accessed 20 Nov. 2025).",
            font_size=12,
        )

        # Stack them top->bottom with tight spacing
        items = VGroup(ref1, ref2, ref3, ref4, ref5, ref6, ref7, ref8).arrange(
            DOWN, buff=0.35, aligned_edge=LEFT
        )
        items.scale(0.95)  # slight shrink to fit nicely
        items.to_edge(LEFT).shift(DOWN * 0.1)

        # Fade in from top to bottom
        for r in items:
            self.play(FadeIn(r, shift=UP * 0.25), run_time=0.05)
            self.wait(0.05)


        t = Text("Images", font_size=30)
        self.play(FadeIn(t))
        self.play(t.animate.to_corner(UR).shift(LEFT*0.5), run_time=0.1)

        ref1 = Tex(
            r"Figure 1: Patriot system --- U.S. Army Missile Command / Redstone Arsenal "
            r"(\texttt{history.redstone.army.mil})",
            font_size=12,
        )

        ref2 = Tex(
            r"Figure 2: Patriot system operated in Operation Desert Storm (1991) --- "
            r"U.S. Army Missile Command / Redstone Arsenal "
            r"(\texttt{history.redstone.army.mil})",
            font_size=12,
        )

        ref3 = Tex(
            r"Figure 3: Launcher station --- Ken H. / Wikimedia Commons (CC BY-SA 4.0)",
            font_size=12,
        )

        ref4 = Tex(
            r"Figure 4: Power generator --- Ministerie van Defensie / Wikimedia Commons (CC BY-SA 4.0)",
            font_size=12,
        )

        ref5 = Tex(
            r"Figure 5: Antenna --- JASDF / Wikimedia Commons (CC BY-SA 4.0)",
            font_size=12,
        )

        ref6 = Tex(
            r"Figure 6: Engagement control station --- JASDF / Wikimedia Commons (CC BY-SA 4.0)",
            font_size=12,
        )

        ref7 = Tex(
            r"Figure 7: Radar set --- JASDF / Wikimedia Commons (CC BY-SA 4.0)",
            font_size=12,
        )

        ref8 = Tex(
            r"Figure 8: Raytheon logo --- \texttt{rtx.com/news/campaigns/raytheon-anschuetz}",
            font_size=12,
        )

        ref9 = Tex(
            r"Figure 9: U.S. Army logo --- "
            r"\texttt{commons.wikimedia.org/wiki/File:Mark\_of\_the\_United\_States\_Army.svg}",
            font_size=12,
        )

        ref10 = Tex(
            r"Figure 10: U.S. flag --- "
            r"\texttt{en.wikipedia.org/wiki/File:Flag\_of\_the\_United\_States.svg}",
            font_size=12,
        )

        # Stack them top->bottom with tight spacing
        items = VGroup(
            ref1, ref2, ref3, ref4, ref5, ref6, ref7, ref8, ref9, ref10
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)

        items.scale(0.95)
        items.to_edge(RIGHT).shift(DOWN * 0.1)

        # Fade in each reference
        for r in items:
            self.play(FadeIn(r, shift=UP * 0.25), run_time=0.05)
            self.wait(0.05)

        self.wait(2)


