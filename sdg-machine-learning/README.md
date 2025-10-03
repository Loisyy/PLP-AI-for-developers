# ThreadCycle — AI for Textile Waste Reduction (SDG 12)

ThreadCycle classifies garment type and condition from a smartphone photo and recommends whether to donate, repair/upcycle, or recycle the item.

## Demo
- Screenshot 1: app home + example prediction
- Screenshot 2: recommendation & upcycling tips

## Quickstart
1. `pip install -r requirements.txt`
2. Run training notebook: `notebooks/02_train_model.ipynb`
3. Run demo: `streamlit run app/streamlit_app.py`

## Files
- notebooks/: data preparation & training
- src/: training and inference scripts
- app/: demo app
- assets/: sample images & screenshots
cd 