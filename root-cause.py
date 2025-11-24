import sys

from manim import *
import math

tmpl = TexTemplate()
tmpl.add_to_preamble(r"""
\usepackage[dvipsnames]{xcolor}

\definecolor{cyan}{HTML}{29ABCA}
\definecolor{red}{HTML}{FF6F00}
""")

# class RootCause1(Scene):
#     def construct(self):
#         title = Text("Root cause", font_size=44)
#         self.play(Write(title))

class RootCause2(Scene):
    def construct(self):
        title = Text("Binary numbers", font_size=50)

        l = Tex(r"""
            \begin{itemize}
                \item Integers $$
                    0_2, 1_2, 10_2, 11_2, 100_2 \ldots
                $$

                \item Fixed point $$ \begin{aligned}
                    {\color{red} 101} & . & {\color{cyan} 011}_2 & \\
                    {\color{red} 101} &   & {\color{cyan} 011}_2 & { \color{gray} / 16_10 }
                \end{aligned} $$

                \item Floating point - {\color{red} mantissa} and {\color{cyan} exponent} $$ \begin{aligned}
                    =& {\color{red} 101.011_2} \\
                     & {\color{red} 1.01011_2}e{\color{cyan} 8_{10}}
                \end{aligned} $$

            \end{itemize}
        """, tex_template=tmpl, font_size=32)

        ex = Code(code_string=r"""
>>> 0.1 + 0.2 == 0.3
False
>>> 9007199254740992.0 + 1.0
9007199254740992.0""", paragraph_config=dict(font_size=12))

        ex.next_to(l, DOWN)

        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP), run_time=0.6)

        self.play(Write(l))
        self.play(FadeIn(ex))

class RootCause3(Scene):
    def construct(self):
        title = Text("Infinite fractions", font_size=50)

        l = Tex(r""" $$\begin{aligned}
            \frac{1}{10}_{10} &= 0.00011001100110011001100\ldots_{2} \\
            \frac{1}{3}_{10}  &= 0.333333\ldots_{10}
        \end{aligned}$$ """, tex_template=tmpl)

        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP), run_time=0.6)

        self.play(Write(l))

class RootCause4(Scene):
    def construct(self):
        title = Text("Floating point precision", font_size=50)

        ex = Code(code_string=r"""
>>> 9007199254740992.0 + 1.0
9007199254740992.0""", paragraph_config=dict(font_size=12))


        l = Tex(r""" $$\begin{aligned}
             & {\color{red} 1.01011_2}e{\color{cyan} 8_{10}} \\
            =& {\color{red} \leavevmode \hbox to 7em { \hfill $ 101.011_2 $ }}
        \end{aligned}$$ """, tex_template=tmpl)

        l.next_to(ex, DOWN)

        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP), run_time=0.6)

        self.play(FadeIn(ex))
        self.play(Write(l))

        for (n, e) in [
            (r"    1010.11{\color{yellow} 0}", 16),
            (r"   10101.1{\color{yellow} 00}", 32),
            (r"  101011.{\color{yellow} 000}", 64),
            (r" 101011{\color{yellow} 0.000}", 128),
            (r"101011{\color{yellow} 00.000}", 256),
        ]:

            l1 = Tex(r""" $$\begin{aligned}
                 & {\color{red} 1.01011_2}e{\color{cyan} """ + str(e) + r"""_{10}} \\
                =& {\color{red}  \leavevmode \hbox to 7em { \hfill $ """ + n + r"""_2 $ }}
            \end{aligned}$$ """, tex_template=tmpl)

            l1.next_to(ex, DOWN)

            self.play(Transform(l, l1))
            self.pause()
            # l = l1

class RootCause5(Scene):
    def construct(self):
        title = Text("Displacement", font_size=50)

        l = Tex(r""" $$\begin{aligned}
            d =& \Delta t * v \\
            d =& (t_1 - t_0) * v \\
            d =& t_1 * v - t_0 * v
        \end{aligned}$$ """, tex_template=tmpl)


        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP), run_time=0.6)

        self.play(Write(l))

        l1 = Tex(r""" $$\begin{aligned}
            d =& \Delta t * v \\
            d =& ( 101011{\color{yellow} 00.000} - 101010{\color{yellow} 00.000} ) * v \\
            d =& 101011{\color{yellow} 00.000} * v - 101010{\color{yellow} 00.000}  * v
        \end{aligned}$$ """, tex_template=tmpl)

        self.pause()
        self.play(Transform(l, l1))

        l1 = Tex(r""" $$\begin{aligned}
            d =& \Delta t * v \\
            d =& 100.000 * v \\
            d =& 101011{\color{yellow} 00.000} * v - 101010{\color{yellow} 00.000}  * v
        \end{aligned}$$ """, tex_template=tmpl)

        self.pause()
        self.play(Transform(l, l1))

