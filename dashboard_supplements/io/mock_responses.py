"""Load mock responses."""
import pandas as pd


def load_fake_response_df(path: str) -> pd.DataFrame:
    """Load sample response dataframe for the given path."""
    output_df = pd.read_csv(path, index_col="Unnamed: 0")
    return output_df


FAKE_PFR_RESPONSE_DF = load_fake_response_df(
    path="./dashboard_supplements/assets/sample_results/sample_pfr_results.csv"
)
FAKE_LIFE_EVENT_RESPONSE_DF = load_fake_response_df(
    path="./dashboard_supplements/assets/sample_results/sample_life_events_results.csv"
)
FAKE_AUTO_PREFILL_RESPONSE_DF = load_fake_response_df(
    path="./dashboard_supplements/assets/sample_results/sample_auto_prefill_results.csv"
)
FAKE_LIFE_PREFILL_RESPONSE_DF = load_fake_response_df(
    path="./dashboard_supplements/assets/sample_results/sample_life_prefill_results.csv"
)
FAKE_SMB_RESPONSE_DF = load_fake_response_df(
    path="./dashboard_supplements/assets/sample_results/sample_smb_results.csv"
)

api_to_fake_response_df_mapper = {
    "PFR": FAKE_PFR_RESPONSE_DF,
    "LifeEvents": FAKE_LIFE_EVENT_RESPONSE_DF,
    "AutoPrefill": FAKE_AUTO_PREFILL_RESPONSE_DF,
    "LifePrefill": FAKE_LIFE_PREFILL_RESPONSE_DF,
    "SMB": FAKE_SMB_RESPONSE_DF,
}
