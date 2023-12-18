bands_sentinel2 = {
    "B01": ["coastal_aerosol"],
    "B02": ["blue"],
    "B03": ["green"],
    "B04": ["red"],
    "B05": ["red_edge_1"],
    "B06": ["red_edge_2"],
    "B07": ["red_edge_3"],
    "B08": ["nir", "nir_1"],
    "B8A": ["nir_narrow", "nir_2"],
    "B09": ["water_vapour"],
    "B11": ["swir_1", "swir_16"],
    "B12": ["swir_2", "swir_22"],
    "AOT": ["aerosol_optical_thickness"],
    "WVP": ["scene_average_water_vapour"],
    "SCL": ["mask", "qa"],
}
bands_ls5_7_sr = {
    "SR_B1": ["blue"],
    "SR_B2": ["green"],
    "SR_B3": ["red"],
    "SR_B4": ["nir"],
    "SR_B5": ["swir_1"],
    "SR_B7": ["swir_2"],
    "QA_PIXEL": ["pq"],
    "SR_ATMOS_OPACITY": ["atmospheric_opacity"],
}

bands_ls8_9_sr = {
    "SR_B2": ["blue"],
    "SR_B3": ["green"],
    "SR_B4": ["red"],
    "SR_B5": ["nir"],
    "SR_B6": ["swir_1"],
    "SR_B7": ["swir_2"],
    "qa_pixel": ["pq"],
    "SR_QA_AEROSOL": ["aerosol_level"],
}

bands_ls_geomad = {
    "blue": ["band_2"],
    "green": ["band_3"],
    "red": ["band_4"],
    "nir08": ["nir", "band_5"],
    "swir16": ["swir1", "swir_1", "band_6"],
    "swir22": ["swir2", "swir_2", "band_7"],
    "smad": ["sdev"],
    "emad": ["edev"],
    "bcmad": ["bcdev"],
    "count": [],
}