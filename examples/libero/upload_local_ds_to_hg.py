from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

# Path to your saved dataset
dataset_path = "/mnt/arc/yygx/pkgs_baselines/openpi/data/huggingface/lerobot/yygx/libero90"
dataset_path = "/home/yygx/.cache/huggingface/lerobot/yygx/libero90"

# Load dataset
dataset = LeRobotDataset.load(dataset_path)

# Check dataset info
print(dataset)

# Push dataset to Hugging Face Hub
dataset.push_to_hub(
    repo_id="yygx/libero90",  # Change to your Hugging Face repo name
    tags=["libero", "panda", "rlds"],
    private=False,  # Set to True if you want it private
    push_videos=True,  # Upload videos if available
    license="apache-2.0",
)
