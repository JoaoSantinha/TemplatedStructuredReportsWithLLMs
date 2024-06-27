TEMPLATE = """The following text is the structure of a radiological report for CT Colonography:\n\
Indication:\n\
    ● [Screening [asymptomatic, average/moderate risk]/\n\
    ● Surveillance [asymptomatic, high risk]/\n\
    ● Diagnostic examination in symptomatic patient [abdominal pain, diarrhea, constipation, gastrointestinal bleeding, anemia, intestinal obstruction, weight loss]/\n\
    ● Following incomplete colonoscopy/\n\
    ● Unable to undergo colonoscopy/\n\
    ● Follow-up in patient with a colonic stoma or after colectomy/\n\
    ● Prior to laparoscopic surgery for colorectal cancer]\n\
Technique: Preparation technique:\n\
    ● Laxative: [PEG/magnesium citrate/sodium phosphate]\n\
    ● Tagging regimen: [iodinated contrast media [..] mL/barium [..] mL/none]\n\
    ● Spasmolytics: [none/hyoscine-N-butylbromide/glucagon]\n\
    ● Insufflation: [manual/electronic] [air/CO2]\n\
    ● Positions: [supine and prone/supine, prone and decubitus/right and left decubitus]\n\
    ● Intravenous contrast media: [no/yes [ ] mL]\n\
    ● Adverse events: [none/angina/arrhythmia/hypertension/hypotension/perforation/bleeding/other]\n\
Visibility of the colonic mucosa: [complete/incomplete due to fecal residue in cecum/ascending/transverse/ descending/sigmoid/rectum/incomplete due to suboptimal distention of cecum/ascending/transverse/ descending/sigmoid/rectum]\n\
Findings:\n\
Colonic anatomy: [normal, abnormal] (specify abnormality).\n\
Colonic abnormalities: [benign strictures/diverticula/extrinsic compression, ...] Colonic lesion (specify for each lesion):\n\
    ● Shape: [sessile/pedunculated/flat]\n\
    ● Attenuation: [soft tissue/fat]\n\
    ● Maximum diameter: [ ] mm, (polyps ≥ 6 mm are reported)\n\
    ● Location: [cecum/ascending colon/transverse colon/descending colon/sigmoid colon/rectum]\n\
Colonic mass (specify for each lesion):\n\
    ● Shape: [annular, semiannular, vegetating)\n\
    ● Maximum diameter: [ ] mm\n\
    ● Location: [cecum/ascending colon/transverse colon/descending colon/sigmoid colon/rectum]\n\
Extracolonic finding (specify for each):\n\
    ● [size, location, lesion features]\n\
    ● [anatomic variant/clinically unimportant/likely unimportant finding, incompletely evaluated/\n\
    potentially important finding]\n\
Conclusion:\n\
Summary of lesions: [normal colon/benign lesions/indeterminate polyp/likely malignant lesions] Extracolonic lesion: [absent/anatomic variant/clinically unimportant/likely unimportant finding, incom- pletely evaluated/potentially important finding]\n\
Recommendation on follow-up: [routine screening/surveillance/colonoscopy/surgical referral]
"""