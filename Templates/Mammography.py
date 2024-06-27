TEMPLATE = """The following text is the structure of a radiological report for a mammography report:\n\
Indication\n\
    * Screening\n\
    * Diagnostic\n\
    * Follow-up\n\
* Patient’s history\n\
* Ultrasound performed?\n\
    * Targeted to a specific location or supplementary screening\n\
Breast composition\n\
* A: Entirely fatty\n\
* B: scattered areas of fibroglandular density\n\
* C: heterogeneously dense, which may obscure small masses\n\
* D: extremely dense, which lowers the sensitivity\n\
Findings\n\
- Location of lesions\n\
    * laterality\n\
    * quadrant and clock face\n\
    * depth\n\
    * distance from the nipple\n\
- Masses\n\
    * shape\n\
        * round\n\
        * oval\n\
        * irregular\n\
    * margin\n\
        * circumscribed\n\
        * obscured\n\
        * microlobulated\n\
        * indistinct\n\
        * spiculated\n\
    * density\n\
        * high density\n\
        * equal density\n\
        * low density\n\
        * fat-containing\n\
- Asymmetry \n\
        * asymmetry\n\
        * global\n\
        * focal\n\
        * developing\n\
- Architectural distortion\n\
    * Distorted parenchyma with no visible mass [Yes/No]\n\
- Calcifications\n\
    * morphology\n\
        * typically benign\n\
            * skin\n\
            * vascular\n\
            * coarse or popcorn-like\n\
            * large rod-like\n\
            * round\n\
            * rim\n\
            * dystrophic\n\
            * milk of calcium\n\
            * suture\n\
        * suspicious morphology\n\
            * amorphous\n\
            * coarse heterogeneous\n\
            * fine pleomorphic\n\
            * fine linear or fine-linear branching\n\
    * distribution\n\
        * diffuse\n\
        * regional\n\
        * grouped\n\
        * linear\n\
        * segmental\n\
- Other findings\n\
    * intramammary lymph node\n\
    * skin lesion\n\
    * solitary dilated duct\n\
- Associated features\n\
    * skin retraction\n\
    * nipple retraction\n\
    * skin thickening\n\
    * trabecular thickening\n\
    * axillary adenopathy\n\
    * architectural distortion\n\
    * calcifications\n\
BI-RADS Final Assessment\n\
* Category\n\
* Management
"""