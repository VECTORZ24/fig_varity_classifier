import pandas as pd

cultivar_schema = {
    "cultivar_id": ("Unique ID, e.g. TN-ZIDI", "str", None),
    "local_names": ("All known names, separated by ';'", "str", None),
    "origin_country": ("Country where the cultivar originates", "TN/MA/DZ/EG/other", None),
    "fig_type": ("Pollination type", "common/smyrna/san_pedro/caprifig", None),
    "main_use": ("Best use", "fresh/dried/both", None),
    "skin_color": ("Skin color", "green/yellow/brown/purple/black", None),
    "pulp_color": ("Pulp color", "white/amber/pink/red", None),
    "fruit_weight_g": ("Average fruit weight", "float", "g"),
    "sugar_brix": ("Sugar content", "float", "°Brix"),
    "shelf_life_days": ("Fresh storage life", "float", "days"),
    "bearing_start_year": ("First harvest after planting", "int", "years"),
    "full_production_year": ("Year reaching full production", "int", "years"),
    "yield_kg_per_tree": ("Typical mature yield, fresh fruit", "float", "kg"),
    "harvest_window": ("Main harvest months", "e.g. 'Aug-Oct'", None),
    "min_temp_tolerance_c": ("Lowest survivable temperature", "float", "°C"),
    "drought_tolerance": ("Rain-fed viability", "low/medium/high", None),
    "salinity_tolerance": ("Tolerance to saline soil/water", "low/medium/high", None),
    "rain_splitting_risk": ("Fruit splitting/souring if rain at ripening", "low/medium/high", None),
    "pest_disease_susceptibility": ("Overall sensitivity (mosaic, fruit fly, rust)", "low/medium/high", None),
}
COLS = list(cultivar_schema)
IDENTITY = {"cultivar_id", "local_names", "origin_country"}

def R(cid, names, country, ftype, use, skin, pulp, wt, brix, shelf, bear, full, yld,
      harv, tmin, dr, sal, rain, pest, doc=""):
    """doc = comma-separated fields that come directly from the PDF.
    Every other non-identity field is an estimate and is listed in estimated_fields."""
    vals = [cid, names, country, ftype, use, skin, pulp, wt, brix, shelf, bear, full, yld,
            harv, tmin, dr, sal, rain, pest]
    row = dict(zip(COLS, vals))
    documented = {d.strip() for d in doc.split(",") if d.strip()}
    row["estimated_fields"] = ";".join(c for c in COLS if c not in IDENTITY and c not in documented)
    return row

M = "medium"
rows = [
    # ---------------- Tunisia ----------------
    R("TN-KHARTOUMI", "Khartoumi;Khartouma", "TN", "smyrna", "dried", "brown", "amber", 35, 20, 3, 3, 7, 25, "Aug-Sep", -10, M, M, M, M, "main_use"),
    R("TN-ZIDI", "Zidi;Zidi Siyah", "TN", "smyrna", "both", "black", "red", 40, 20.5, 4, 3, 7, 30, "Aug-Oct", -10, "high", M, M, M, "fig_type,main_use,skin_color,pulp_color,fruit_weight_g,sugar_brix"),
    R("TN-BOUHOULI", "Bouhouli;Figue de Djebba", "TN", "common", "both", "purple", "red", 55, 17, 4, 3, 7, 30, "Jun-Jul; Aug-Sep", -10, M, M, M, M, "fig_type,main_use,skin_color,pulp_color,fruit_weight_g,harvest_window"),
    R("TN-WAHCHI", "Wahchi;El Wahchi", "TN", "common", "both", "yellow", "pink", 50, 19, 3, 3, 7, 25, "Aug-Oct", -10, "high", M, M, M, "main_use,skin_color,pulp_color,drought_tolerance"),
    R("TN-BIDHI", "Bidhi", "TN", "smyrna", "both", "yellow", "amber", 52, 20, 4, 3, 7, 30, "Aug-Sep", -8, "high", "high", M, M, "fig_type,skin_color,fruit_weight_g"),
    R("TN-BITHER-ABIOD", "Bither Abiod;Bither Abiad", "TN", "san_pedro", "both", "green", "amber", 45, 19, 4, 3, 7, 25, "Jun-Jul; Aug-Oct", -8, "high", "high", M, M, "fig_type,skin_color"),
    R("TN-BITHER-AKHAL", "Bither Akhal", "TN", "san_pedro", "both", "black", "red", 45, 19, 4, 3, 7, 25, "Jun-Jul; Aug-Oct", -8, "high", "high", M, M, "fig_type,skin_color"),
    R("TN-CHETOUI", "Chetoui;Shtoui;Chetoui d'Algérie", "TN;DZ", "common", "both", "green", "red", 50, 20, 4, 3, 7, 30, "Jun-Jul; Sep-Oct", -8, M, M, "low", M, "fig_type,main_use,skin_color,pulp_color,fruit_weight_g,harvest_window,rain_splitting_risk"),
    # ---------------- Algeria ----------------
    R("DZ-AZEGZAW", "Azegzaw;Zegzaw;Azagzaou", "DZ", "common", "both", "green", "amber", 40, 20, 4, 3, 7, 25, "Sep", -10, M, M, M, M, "harvest_window"),
    R("DZ-BLACK-ALGIERS", "Black Algiers;Noire d'Alger;Lekhal", "DZ", "common", "fresh", "black", "red", 40, 20, 4, 3, 7, 30, "May-Jun; Aug-Oct", -8, M, M, M, M, "fig_type,skin_color,pulp_color,fruit_weight_g,harvest_window"),
    R("DZ-TAAMRIWT", "Taamriwt;Taamriwth;Tameriout;Taâmriout;Taamriout;Tameryut", "DZ", "common", "dried", "yellow", "amber", 45, 22, 3, 3, 8, 20, "Aug-Sep", -10, "high", M, M, M, "main_use"),
    R("DZ-MARABOUT", "Marabout;Sultane du Marabout;Aseltani", "DZ;TN", "smyrna", "both", "black", "red", 55, 22, 4, 3, 7, 35, "Aug-Oct", -10, M, M, "low", M, "fig_type,skin_color,pulp_color,min_temp_tolerance_c,rain_splitting_risk"),
    # ---------------- Egypt ----------------
    R("EG-FAYUMI", "Fayumi;Fayoumi;Black Iranian;Hava;Sultani", "EG", "common", "fresh", "purple", "red", 60, 18, 3, 2, 5, 25, "Jun-Aug", -5, M, M, "high", M, "skin_color,pulp_color,min_temp_tolerance_c"),
    # ---------------- Morocco ----------------
    R("MA-ABOUCHERCHAOU", "Aboucherchaou", "MA", "common", "both", "green", "red", 55, 19, 4, 3, 7, 30, "Jul", -8, M, M, "high", M, "fig_type,skin_color,pulp_color,harvest_window"),
    R("MA-AOUNQ-HMAM", "Aounq Hmam;Aâounq el Hmam;Ounq Hmam;Ounq Lhmam;Onk Hmam", "MA", "common", "both", "purple", "red", 58, 20, 4, 3, 7, 30, "Jun-Jul; Aug-Sep", -8, M, M, M, M, "fruit_weight_g,sugar_brix,harvest_window"),
    R("MA-BAKOR", "Bakor", "MA;DZ;TN", "common", "both", "black", "amber", 40, 20, 3, 3, 7, 25, "Jun; Aug-Oct", -10, M, M, M, M, "skin_color,pulp_color,harvest_window"),
    R("MA-CHAARI", "Chaari;Chaâri", "MA", "common", "both", "purple", "red", 45, 19, 4, 3, 7, 25, "Sep-Oct", -8, M, M, M, M, ""),
    R("MA-FASSI", "Fassi;Khadri Lak'hal;Fassi Kahli", "MA", "common", "both", "black", "red", 40, 19, 4, 3, 7, 30, "Aug-Oct", -8, "high", M, M, M, "skin_color,drought_tolerance"),
    R("MA-FILALIA", "Filalia;Filali;Figue du Tafilalet", "MA", "common", "both", "purple", "red", 40, 20, 4, 3, 7, 30, "Aug-Oct", -8, M, M, M, M, ""),
    R("MA-GHOUDANE", "Ghoudane;Ghouddane;El Ghoddane;Rhouddan;Rhouddane;Ghouddane l'hor", "MA", "common", "both", "purple", "amber", 40, 19, 4, 3, 7, 35, "Jun-Jul; Aug-Oct", -8, M, M, "low", M, "fig_type,main_use,skin_color,rain_splitting_risk"),
    R("MA-HAMOURI", "Hamouri", "MA", "common", "both", "brown", "red", 45, 19, 4, 3, 7, 25, "Aug-Oct", -8, M, M, M, M, "main_use,skin_color"),
    R("MA-HAMRI", "Hamri;Hamri Rkiwake;Noukal;Hamri de Meknès", "MA", "common", "fresh", "brown", "red", 44, 17, 4, 3, 7, 37, "May-Jun; Jul-Aug", -8, M, M, M, M, "main_use,skin_color,pulp_color,fruit_weight_g,sugar_brix,yield_kg_per_tree,harvest_window"),
    R("MA-KAHOULI", "Kahouli;Kehli;Kohli", "MA", "common", "both", "black", "red", 35, 16, 4, 3, 7, 25, "Aug-Oct", -8, M, M, M, M, "skin_color"),
    R("MA-KOTE", "Koté;Kouti;El Koté;Koté Hamdi;Harcha", "MA", "common", "dried", "purple", "amber", 40, 21, 3, 3, 7, 25, "Aug-Oct", -8, M, M, M, M, "main_use"),
    R("MA-LASSOUNE", "Lassoune;Lassoun", "MA", "common", "fresh", "purple", "red", 40, 19, 4, 3, 7, 25, "Aug-Oct", -8, M, M, M, M, "main_use"),
    R("MA-LEMBDAR-LABIAD", "Lembdar Labiad;Lembdar blanc;Lemdar Lbyed", "MA", "san_pedro", "fresh", "yellow", "amber", 40, 19, 4, 3, 7, 30, "Jun-Jul; Aug-Sep", -8, M, M, M, M, "main_use,skin_color"),
    R("MA-LEMBDAR-LAKHAL", "Lembdar Lakhal;Lembdar Noir;Bacora;Lemdar", "MA;DZ", "san_pedro", "both", "black", "red", 40, 19, 4, 3, 7, 30, "Jun-Jul; Aug-Sep", -8, M, M, M, M, "fig_type,skin_color,harvest_window"),
    R("MA-JOHRI", "Johri;El Johri;El Messari;Messari;Homrane;Homran;Lamtel;Mtioui", "MA", "san_pedro", "both", "green", "red", 45, 19, 4, 3, 7, 30, "Jun-Jul; Aug-Sep", -8, M, M, M, M, "fig_type,main_use,skin_color,pulp_color,harvest_window"),
    R("MA-NABOUT", "Nabout;Nabut", "MA", "common", "dried", "green", "amber", 35, 21, 3, 3, 7, 25, "Aug-Oct", -8, M, M, M, M, "main_use,skin_color"),
    R("MA-OURNAKSSI", "Ournakssi;Ournaksi;Wernaksi;Wernaxsi", "MA", "common", "both", "green", "amber", 45, 19, 4, 3, 7, 30, "May-Jun; Aug-Sep", -10, M, M, M, M, "skin_color"),
]

cultivars = pd.DataFrame(rows, columns=COLS + ["estimated_fields"])

# keep a single name per cultivar: the first entry of the ';'-separated list
cultivars["local_names"] = cultivars["local_names"].str.split(";").str[0].str.strip()

# ---- validation of allowed values ----
allowed = {
    "fig_type": {"common", "smyrna", "san_pedro", "caprifig"},
    "main_use": {"fresh", "dried", "both"},
    "skin_color": {"green", "yellow", "brown", "purple", "black"},
    "pulp_color": {"white", "amber", "pink", "red"},
    "drought_tolerance": {"low", "medium", "high"},
    "salinity_tolerance": {"low", "medium", "high"},
    "rain_splitting_risk": {"low", "medium", "high"},
    "pest_disease_susceptibility": {"low", "medium", "high"},
}
for col, ok in allowed.items():
    bad = set(cultivars[col]) - ok
    assert not bad, f"{col}: invalid values {bad}"
assert cultivars["cultivar_id"].is_unique
assert cultivars[COLS].notna().all().all()

if __name__ == "__main__":
    cultivars.to_csv("/mnt/user-data/outputs/fig_cultivars.csv", index=False, encoding="utf-8-sig")
    n_est = cultivars["estimated_fields"].str.count(";") + 1
    print(cultivars.shape, "rows x cols")
    print("avg estimated fields per row:", round(n_est.mean(), 1), "of", len(COLS) - len(IDENTITY))
    print(cultivars[["cultivar_id", "fig_type", "main_use", "skin_color", "pulp_color"]].to_string(index=False))
