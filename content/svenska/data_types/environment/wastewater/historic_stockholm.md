---
title: "Historic data for Stockholm"
toc: false
---

<div class="alert alert-info">
    <i class="fas fa-exclamation-triangle"></i> Svensk översättning för de engelska texterna kommer inom kort.</span>
</div>

This page displays data on the amount of SARS-CoV-2 in Stockholm between April 2020 and August 2021 calculated as Gene copy number/week (raw wastewater) with bovine + PMMoV factor. From September 2021 onwards, the method was changed. Please [see this page for the most recent data](../).

This project, led by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology; zeynepcg@kth.se), is a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater, started in mid-April 2020, from Bromma, Henriksdal, and Käppala wastewater treatment plants (WWTP). These treatment plants receive wastewater from a population of approximately 360,000; 860,000 and 500,000, respectively. Please consult [this map for the exact catchment area of the wastewater collection channels in Käppala](/wastewater/map_Kappala.pdf) and [this map for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

After concentration, filtering, and preparation, the samples are analyzed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)). In some cases, the raw wastewater has been frozen at –20 degrees, and  concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues is based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. The study concluded that the double ultrafiltration method adapted by KTH has a significantly higher efficiency compared to single filtration and adsorption methods. For detailed information about the concentration method, see the publication.

See also [the page of the research group where summaries of data and preliminary conclusions are presented](https://www.kth.se/water/research/covid-1.979048).

**Download the data:** [Gene copy number/week (raw wastewater) with bovine + PMMoV factor; Excel file.](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Stockholm.xlsx) Numbers for Stockholm overall and divided by Inlet Henriksdal, Sickla, Hässelby, Järva, Riksby, and Käppala are available. Results are available (partially) starting from week 16 of 2020 and until week 34 of 2021.

**How to cite:**
Cetecioglu Z G, Williams, C, Khatami, K, Atasoy, M, Nandy, P, Jafferali, M H, Birgersson, M. SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483) (2021).

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="stockholm_combined"></div>
</div>

<div class="small text-muted">*NB: All samples until week 21 of 2020 were received by the lab in week 21. Between weeks 21 and 33 of 2020 samples were analyzed biweekly. After week 33 of 2020, samples were analysed weekly.</div>

<div class="small text-muted">**NB: Measurements were taken fortnightly, rather than weekly, between weeks 24 and 32 of 2021.</div>

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.1.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/956f9390690043b8ae5f62b90d22f84f.js?id=stockholm_combined"></script>
