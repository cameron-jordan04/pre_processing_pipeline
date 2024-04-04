from pre_processing import Preprocess


def fit_reference(
    raw_reference,
    raw_signal,
    fr,
    drop=200,
    window_size=11,
    r_squared_threshold=0.7,
    smoothing_method="tma",
    baseline_method="lpf",
    fit_method="l",
    detrend_last=False,
):
    """
    Input:
        fr: sampling frequency
    Using preprocessing method in Preprocess object, fit reference channel to signal channel,
    and produce (z scored) reference, signal, and fitted reference

    Returns:
        fitted_reference: np.ndarray
    """
    pass
