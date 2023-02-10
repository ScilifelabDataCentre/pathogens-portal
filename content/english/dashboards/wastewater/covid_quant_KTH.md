---
title: The amount of SARS-CoV-2 virus in wastewater across Sweden
toc: false
type: wastewater
menu:
    wastewater:
        name: COVID quantification - KTH
        weight: 20
plotly: true
---

## SEEC-KTH: Samples from Stockholm and Malmö

This project, led by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology; zeynepcg@kth.se), is a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH.

Analysis of wastewater samples from Stockholm takes place in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater started in mid-April 2020 from Bromma, Henriksdal, and Käppala wastewater treatment plants. These plants receive wastewater from a population of approximately 360,000; 860,000 and 500,000, respectively. Please consult [this map for the exact catchment area of the wastewater collection channels in Käppala](/wastewater/map_Kappala.pdf) and [this map for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

Wastewater sample collection from the Sjölunda wastewater treatment plant in Malmö started from week 39 of 2021. This plant processes water from the larger part of Malmö as well as from Burlöv municipanity and parts of Lomma, Staffanstorp, and Svedala municipalities. In total, there are around 300 000 people living in the catchment area of this wastewater treatment plant. See [a map of the catchment area and information in this PDF](/wastewater/sjolunda.pdf).

After concentration, filtering, and preparation, the samples are analysed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema *et al.* (2020)](https://doi.org/10.1021/acs.estlett.0c00357)). In some cases, the raw wastewater has been frozen at –20 degrees, and  concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues from the beginning of the project until week 35 of 2021 was based on their published study ([Jafferali *et al.*, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. From week 35 of 2021, the group is using [the Promega kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) for the concentration step.

### Dataset

**Download the data:** [N3-gene copy number per PMMoV gene copy number; Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Results are available (partially) starting from week 16 of 2020 for Stockholm and starting from week 39 of 2021 for Malmö; updated weekly.\
**Contact:** zeynepcg@kth.se

**How to cite dataset:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

### Visualisations: Stockholm

<div class="alert alert-info">Last updated: <span id="last_modified_stockholm"></span></div>

<button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  How to use the interactive features of the plot
</button>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>


### Visusalisations: Malmö

<div class="alert alert-info">Last updated: <span id="last_modified_malmo"></span></div>

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive w-100" id="malmo"></div>
</div>

### Commentary

<div><b>Date:</b> <span id="kth_comment_date"></span><br><b>Commentary:</b> <span id="kth_comment"></span></div>

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/1016b97372e9403da0b8e8e7bb14fa8d.js?id=malmo"></script>
