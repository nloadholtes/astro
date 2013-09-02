import matplotlib.pyplot as plt


def draw(outputname):
    circle1 = plt.Circle((.5, .5), .2, color='b')
    fig = plt.gcf()
    fig.gca().add_artist(circle1)
    plt.savefig(outputname)
