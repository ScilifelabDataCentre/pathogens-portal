---
title: The amount of SARS-CoV-2 virus in wastewater across Sweden
toc: false
---

We present wastewater epidemiology data from four Swedish cities - Uppsala, Stockholm, Umeå, and Örebro, with a total population of 1.5 million people. Wastewater surveillance could prove an effective system for monitoring COVID-19 prevalence and an early warning system for predicting upcoming outbreaks. Note that because different sample collection and data analysis methods are used in different cities, it is not possible to make comparisons of viral load across these cities. Comparisons should be made within each city because the methodology remains the same. [See below for details](#background) on wastewater epidemiology.

<div class="row"><div class="col-lg-7"><p>Below, you can find graphs depicting the amount of SARS-CoV-2 gene copies in waste water in various cities across Sweden and links to download the data behind.</p>
<ul><li><a href="#uppsala">Wastewater in Uppsala</a></li>
<li><a href="#stockholm">Wastewater in Stockholm</a></li>
<li><a href="#umea">Wastewater in Umeå</a></li>
<li><a href="#orebro">Wastewater in Örebro</a></li>
</ul></div><div class="col-lg-5">
{{< wastewater_map >}}
</div></div>

<a id="uppsala"><h2>Amount of SARS-CoV-2 in Uppsala wastewater</h2></a>

This project is run by associate professor Anna J. Székely (SLU, Swedish University of Agricultural Sciences) in collaboration with Uppsala Vatten. The amount of SARS-CoV-2 virus in the wastewater of Uppsala is estimated by analyzing raw wastewater collected at Kungsängsverket, Uppsala Vatten’s main treatment facility. The wastewater treated at the facility is collected by two main wastewater collection channels: one collects the wastewater of approximately 100 000 people from the south-western part of the city (‘AB’), and the other of almost 80 000 people from the north-eastern part of the city (‘C’). Please [consult this map for the exact catchment area of the two wastewater collection channels](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf). A combined measure based on results from both inlets is calculated as well. Measurements are taken weekly, by processing a representative sample collected over 24 hours (i.e., flow compensated sample). The SARS-CoV-2 virus content of the wastewater on the given day is normalized to the fecal matter content to avoid variation from flow differences and population fluctuation.

The samples are processed according to standard methods. Briefly, the viral content of the samples is concentrated according to the modified electronegative filtration method ([method C, Ahmed and colleagues, 2020](https://doi.org/10.1016/j.scitotenv.2020.139960)), viral RNA is extracted using the RNeasy PowerMicrobiome kit (Qiagen) and the copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). The virus recovery efficiency of the process and the presence of potential inhibitors is monitored by adding to the samples bovine coronavirus (BCoV) as process surrogate virus. To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV) which is the most abundant RNA virus in human feces and serves as an estimator of human fecal content ([Symonds and colleagues, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

Note that the scores provided in this dataset and depicted in plots are preliminary. The team is still conducting method efficiency checks that might slightly modify the final results.

**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV per wastewater collection channel and overall on measurement day, Excel file.](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Uppsala.xlsx) Data available starting from week 38 of 2020; updated weekly.

**Principal investigator:** Anna J. Székely, SLU, Swedish University of Agricultural Sciences.  
**Contact:** anna.szekely@slu.se

##### Wastewater collection channels in Uppsala combined

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="uppsala_combined"></div>
</div>

<div class="row ml-1"><a class="btn" data-toggle="collapse" href="#uppsala_ab_plot" role="button" aria-expanded="false" aria-controls="uppsala_ab_plot" style="font-weight: 500">
  Wastewater collection channel AB, south-western part of Uppsala
  <i class="fas fa-caret-down"></i>
</a></div>
<div class="collapse" id="uppsala_ab_plot">
  <div class="card card-body">
    <div class="row"><div class="col">
    <div class="d-md-none alert alert-info">
      Scroll the plot sideways to view all data.
    </div>
    <div class="plot_wrapper">
      <div class="table-responsive" id="uppsala_ab"></div>
    </div>
    </div></div>
  </div>
</div>

<div class="row ml-1"><a class="btn" data-toggle="collapse" href="#uppsala_c_plot" role="button" aria-expanded="false" aria-controls="uppsala_c_plot" style="font-weight: 500">
  Wastewater collection channel C, north-eastern part of Uppsala
  <i class="fas fa-caret-down"></i>
</a></div>
<div class="collapse" id="uppsala_c_plot">
  <div class="card card-body">
    <div class="row"><div class="col">
    <div class="d-md-none alert alert-info">
      Scroll the plot sideways to view all data.
    </div>
    <div class="plot_wrapper">
      <div class="table-responsive" id="uppsala_c"></div>
    </div>
    </div></div>
  </div>
</div>

<a id="stockholm"><h2>Amount of SARS-CoV-2 in wastewater treatment facilities in Stockholm</h2></a>

This project, lead by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology), is a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater, started in mid-April 2020, from Bromma, Henriksdal, and Käppala wastewater treatment plants (WWTP). These treatment plants receive wastewater from a population of approximately 360,000; 860,000 and 500,000, respectively. Please consult [this map for the exact catchment area of the wastewater collection channels in Käppala](/wastewater/map_Kappala.pdf) and [this map for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

After concentration, filtering, and preparation, the samples are analyzed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939). In some cases, the raw wastewater has been frozen at –20 degrees, and  concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues is based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. The study concluded that the double ultrafiltration method adapted by KTH has a significantly higher efficiency compared to single filtration and adsorption methods. For detailed information about the concentration method, see the publication.

See also [the page of the research group where summaries of data and preliminary conclusions are presented](https://www.kth.se/water/research/covid-1.979048).

**Download the data:** [Gene copy number per week in raw wastewater with bovine factor, weekly Ct values of PMMoV; Excel file.](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Stockholm.xlsx) The data is divided by Inlet Henriksdal, Sickla, Hässelby, Järva, Riksby, and Käppala. Data available (partially) starting from week 16 of 2020; updated weekly.

**Principal investigator:** Zeynep Cetecioglu Gurol (KTH Royal Institute of Technology)  
**Contact:** zeynepcg@kth.se

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="stockholm_combined"></div>
</div>

<div class="small text-muted">*NB: All samples until week 21 of 2020 were received by the lab in week 21. Between weeks 21 and 33 of 2020 samples were analyzed biweekly. After week 33 of 2020, samples were analyzed weekly.</div>

<div class="row ml-0 mt-3"><b>Publications:</b></div><div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939
</div></div>

<a id="umea"><h2>Amount of SARS-CoV-2 in Umeå wastewater</h2></a>

This project is run by associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences) in collaboration with the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and associate professor Mette Myrmel at the Norwegian University of Life Sciences. The amount of SARS-CoV-2 virus in the wastewater is measured in the wastewater treatment facility in Umeå. Please [consult this map for the exact catchment area of the wastewater collection channels](/wastewater/map_umeaa.jpg).

After preparation, the viruses were extracted using ultra filtration and analyzed using qPCR technique for SARS CoV-2 RNA. qPCR samples were normalized against PMMV. Until January 2021, three samples per week were taken and their results were pooled to provide a weekly estimate. From February 2021 on, samples are only collected at one time point per week. Primers used to detect the SARS-COV-2 gene (previously used and verified by [Corman and colleagues, 2020](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045)).

The amount of SARS-CoV-2 for each week is measured/depicted compared to the amount of SARS-CoV-2 on November 6 2020.

**Download the data:** [Gene copy number change (%) relative to Nov 6 2020 and flow level at each measurement day and weekly numbers, Excel file.](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Umeaa.xlsx). Data is available starting from week 44 of 2020; updated monthly.

**Principal investigator:** Maja Malmberg (SLU, Swedish University of Agricultural Sciences)  
**Contact:** maja.malmberg@slu.se

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="umea_combined"></div>
</div>

<a id="orebro"><h2>Amount of SARS-CoV-2 in Örebro wastewater</h2></a>

This project is run by associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences) in collaboration with [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and associate professor Mette Myrmel at the Norwegian University of Life Sciences. The amount of SARS-CoV-2 virus in the wastewater is measured in the wastewater treatment facility in Örebro. Please [consult this map for the exact catchment area of the wastewater collection channels](/wastewater/map_orebro.pdf).

After preparation, the viruses were extracted using ultra filtration and analyzed using qPCR technique for SARS CoV-2 RNA. qPCR samples were normalized against PMMV. Until January 2021, three samples per week were taken and their results were pooled to provide a weekly estimate. From February 2021 on, samples are only collected at one time point per week. Primers used to detect the SARS-COV-2 gene (previously used and verified by [Corman and colleagues, 2020](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045)).

 The amount of SARS-CoV-2 for each week is measured/depicted compared to the amount of SARS-CoV-2 on November 6 2020.

**Download the data:** [Gene copy number change (%) relative to Nov 6 2020 and flow level at each measurement day and weekly numbers, Excel file.](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Orebro.xlsx). Data is available starting from week 42 of 2020; updated monthly.

**Principal investigator:** Maja Malmberg (SLU, Swedish University of Agricultural Sciences)  
**Contact:** maja.malmberg@slu.se

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="orebro_combined"></div>
</div>

<a id="background"><h2>Background: Wastewater-based epidemiology</h2></a>

SARS-CoV-2 virus genome can be detected in feces samples from COVID-19 patients using polymerase chain reaction (PCR) (see, for example, [Wu and colleagues, 2020](https://doi.org/10.1016/S2468-1253(20)30083-2)). Monitoring of SARS CoV-2 virus levels in wastewater from communities could therefore provide early surveillance of disease prevalence at a population-wide level, referred to as wastewater-based epidemiology ([Corpuz and colleagues, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Wastewater-based epidemiology studies the amount of virus genome present in the wastewater, measured using PCR technology. Waste water, also referred too as “sewage,” includes water from households or building, kitchen sinks, toilets, showers. However, it could also include water from non-household sources (for example, rainwater and water from industrial use). Samples are periodically taken at wastewater treatment facilities, allowing to make comparisons of the viral load over time. It has previously been shown that the SARS CoV-2 virus content in wastewater can predict increases in infection in the population and follows the epidemic trend measured by the number of COVID-19 cases and hospitalization rate (see [Peccia and colleagues, 2020](https://doi.org/10.1038/s41587-020-0684-z)). During the COVID-19 pandemic, surveillance of viral RNA levels in waste water has become increasingly used to monitor and predict the spread of the disease.

Please note that the graphs presented on this page are based on preliminary and not yet completely evaluated data. The shared data shall therefore be used with caution. Note that because different sample collection and data analysis methods are used in different research projects below (i.e, for different cities), it is not possible to make comparisons of viral load across these projects (i.e, across cities). Comparisons should be made within each project (i.e., city) since the methodology remains the same for different weeks of measurement. Wastewater monitoring should primarily be seen as a monitoring system. Taken together with data for infection testing, intensive care admissions, etc., it may help understanding of the regional dynamics of the COVID-19 pandemic.

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/6d16b18be0d74425b313040c502f29c8.js?id=uppsala_combined"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/20aa7fa76b29428fadc1884c59bc5d0b.js?id=uppsala_ab"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a6de6f328d3d49bf97c2cd9784f012cc.js?id=uppsala_c"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/7db40a88e0f34ea69cebed7a4be51e55.js?id=stockholm_combined"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/030ac237d44248dda87e2c9277a49cc7.js?id=umea_combined"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/fe03ef2220814eeeb3e99eb26a7c46e2.js?id=orebro_combined"></script>
