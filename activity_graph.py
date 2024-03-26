import os
import git
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to collect data on pulls and pushes per day from the repository
def collect_data(repo_path):
    repo = git.Repo(repo_path)
    pulls = {}
    pushes = {}

    for commit in repo.iter_commits('--since="1 week ago"'):
        date = commit.committed_date
        date_str = commit.committed_datetime.strftime('%Y-%m-%d')
        author = commit.author.name

        if author not in pulls:
            pulls[author] = {date_str: 0}
            pushes[author] = {date_str: 0}
        else:
            if date_str not in pulls[author]:
                pulls[author][date_str] = 0
                pushes[author][date_str] = 0

        if commit.summary.startswith('Merge pull request'):
            pulls[author][date_str] += 1
        else:
            pushes[author][date_str] += 1

    return pulls, pushes

# Function to generate an animated activity graph
def generate_activity_graph(pulls, pushes):
    fig, ax = plt.subplots(figsize=(10, 6))

    def update(frame):
        ax.clear()
        ax.set_title('Daily Pulls and Pushes')
        ax.set_xlabel('Date')
        ax.set_ylabel('Count')
        ax.grid(True)

        for author, data in pulls.items():
            ax.plot(list(data.keys()), list(data.values()), label=f'{author} (Pulls)', marker='o')
        for author, data in pushes.items():
            ax.plot(list(data.keys()), list(data.values()), label=f'{author} (Pushes)', marker='s')
        ax.legend(loc='upper left')
        ax.set_xticklabels(ax.get_xticks(), rotation=45, ha='right')

    anim = FuncAnimation(fig, update, interval=1000)
    anim.save('activity_graph.gif', writer='imagemagick')

# Function to update README.md with the link to the animated GIF
def update_readme_with_gif(url):
    # Implement your code to update the README.md here
    pass

if __name__ == "__main__":
    # Get the current working directory of the script
    script_dir = os.getcwd()

    # Navigate to the parent directory of the repository
    repo_path = os.path.dirname(script_dir)

    # Print the repository path
    print(f"Repository Path: {repo_path}")

    # Proceed with the script
    try:
        # Collect data on pulls and pushes per day
        pulls, pushes = collect_data(repo_path)

        # Generate an animated activity graph
        generate_activity_graph(pulls, pushes)

        # Upload the animated GIF to a hosting service and get the URL
        # Replace 'https://example.com/activity-graph.gif' with the actual URL
        # Upload the GIF to GitHub or a third-party image hosting service
        # Retrieve the URL of the uploaded GIF
        gif_url = 'https://github.com/gi88785/noFap/raw/main/activity_graph.gif'

        # Update README.md with the link to the animated GIF
        update_readme_with_gif(gif_url)
    except Exception as e:
        print(f"An error occurred: {e}")
