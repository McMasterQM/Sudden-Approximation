from ..SuddenPinBox import *

import numpy as np
from numpy.testing import assert_equal, assert_allclose


def test_compute_wavefunction():
    np.random.seed(42)
    x = np.random.uniform(size=10)
    n = np.random.randint(100, size=10)
    a = np.random.rand(10) * 10

    answer = []
    for x_, n_, a_ in zip(x, n, a):
        answer.append(compute_wavefunction(x_, int(n_), a_))

    true_answer = [-0.4313390641726634, 0.1466311206999975, 0.0, 0.0, 0.2590084733480005,
                   -0.6960986168854585, 0.7890380993396575, -0.42923268673108556, -0.6266773901732248,
                   -1.3642044541224478]
    assert_allclose(answer, true_answer)


def test_compute_amplitude_numerical():
    np.random.seed(4)
    n0 = np.random.randint(100, size=10)
    m = np.random.randint(100, size=20)[-10:]
    a = np.random.rand(20) * 10
    b = np.random.rand(20) * 20

    answer = []
    for n_, m_, a_, b_ in zip(n0, m, a, b):
        answer.append(compute_amplitude_numerical(int(n_), int(m_), a_, b_))

    true_answer = [-0.0008780870757880217,
                   -0.0013464636548218382,
                   0.17444582335581715,
                   -0.000335126641611293,
                   -0.002934518726569409,
                   0.00048791225601132213,
                   -0.0036982022475510294,
                   0.004570046708198055,
                   0.030501498242461095,
                   -0.05172338841176417]
    assert_allclose(answer, true_answer)

def test_compute_amplitude_analytic():
    np.random.seed(2)
    n0 = np.random.randint(100, size=10)
    a = np.random.rand(20) * 10
    b = np.random.rand(20) * 20
    x =
    t =

    answer = []
    for n_, m_, a_, b_ in zip(n0, m, a, b):
        answer.append(compute_amplitude_analytic(int(n_), int(m_), a_, b_))

    true_answer = [-0.0008780870757880217,
                   -0.0013464636548218382,
                   0.17444582335581715,
                   -0.000335126641611293,
                   -0.002934518726569409,
                   0.00048791225601132213,
                   -0.0036982022475510294,
                   0.004570046708198055,
                   0.030501498242461095,
                   -0.05172338841176417]
    assert_allclose(answer, true_answer)


def test_compute_probability():
    np.random.seed(4)
    n0 = np.random.randint(100, size=20) + 1
    a = np.random.rand(20) * 10
    b = np.random.rand(20) * 20
    x = np.random.uniform(size=20)
    t = np.random.uniform(size=40)[-20:]

    answer = []
    for n_, a_, b_, x_, t_ in zip(n0, a, b, x, t):
        answer.append(compute_probability(int(n_), a_, b_, x_, t_))

    true_answer = [0.8089165765772012,
                 0.01544980862746233,
                 1.233594599222288e-07,
                 0.21356240554778294,
                 1.221532636184804e-05,
                 0.005596394551499151,
                 0.0012102095252264232,
                 0.2001722360532436,
                 0.0001258256620188786,
                 0.029417610913258434,
                 0.00027372598964721704,
                 9.63436400271835e-05,
                 2.6919096864722895e-05,
                 0.010070005154501476,
                 0.048651296425007345,
                 0.00016042491700159016,
                 0.0021168562570437954,
                 0.006874454809915886,
                 0.36925270423996864,
                 1.3305855425309676]

    assert_allclose(answer, true_answer)
