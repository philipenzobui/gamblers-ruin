import numpy as np
import matplotlib.pyplot as plt
import io
import imageio.v2 as imageio

def simulate(p, n1, n2):
    rounds = 0
    while(n1 > 0 and n2 > 0):
        rounds = rounds + 1
        if np.random.uniform() < p: 
            n1 = n1 + 1; n2 = n2 - 1
        else: 
            n1 = n1 - 1; n2 = n2 + 1
    winner = "P1" if n1 != 0 else "P2"
    return winner

def prob(p, n1, n2):
    return (1-((1-p)/p)**(n1))/(1-((1-p)/p)**(n1+n2))

wins, wins2 = 0, 0
win_percentages1, win_percentages2 = [], []
euro_roulette = 18/37
ame_roulette = 18/38
n1 = 10
n2 = 10

theo_euro = prob(euro_roulette, n1, n2)
theo_ame = prob(ame_roulette, n1, n2)

iterations = 100000

images = []

print(f"European roulette theoretical win percentange : {theo_euro:.6f}")
print(f"American roulette theoretical win percentange : {theo_ame:.6f}")

plt.ioff()

for i in range(1, iterations + 1):
    if simulate(euro_roulette, n1, n2) == "P1": wins += 1
    if simulate(ame_roulette, n1, n2) == "P1": wins2 += 1
    win_percentage1 = wins / i
    win_percentage2 = wins2 / i
    win_percentages1.append(win_percentage1)
    win_percentages2.append(win_percentage2)

    if((i < 1000 and i % 10 == 0) or (i < 10000 and i % 100 == 0) or (i < 100000 and i % 1000 == 0)):
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.plot(range(1, i + 1), win_percentages1, color = 'salmon')
        ax.plot(range(1, i + 1), win_percentages2, color = 'seagreen')
        ax.set_xlabel('Number of Rounds')
        ax.set_ylabel('Win Percentage')
        ax.set_title('Win Percentage Comparison')

        label1 = f'European roulette: {win_percentages1[i-1]:.6f}'
        label2 = f'American roulette: {win_percentages2[i-1]:.6f}'
        ax.text(0.98, 0.10, label1, horizontalalignment='right', verticalalignment='bottom', 
                transform=ax.transAxes)
        ax.text(0.98, 0.05, label2, horizontalalignment='right', verticalalignment='bottom', 
                transform=ax.transAxes)


        # Capture the plot image data in memory
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)  # Reset the buffer position

        # Read the plot image from memory and append it to the list
        image = imageio.imread(buffer)
        plt.close(fig)  # Close the current plot to release memory
        buffer.close()  # Close the buffer

        # Append the image to the list
        images.append(image)

for _ in range(5 * 20):  # 5 seconds at 10 fps
    images.append(image)

imageio.mimsave('win_percentage.gif', images, fps=20)


