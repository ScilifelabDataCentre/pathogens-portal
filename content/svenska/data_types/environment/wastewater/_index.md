---
title: The amount of SARS-CoV-2 virus in wastewater across Sweden
toc: true
menu:
  other_data:
      name: Environment
      identifier: environment
      weight: 50
plotly: true
---

<div class="alert alert-info">
    <i class="fas fa-exclamation-triangle"></i> Svensk översättning för de engelska texterna kommer inom kort.</span>
</div>

Vi presenterar epidemiologiska data av mätningar av SARS-CoV-2 virus i avloppsvatten från olika svenska städer med totalt över 1.5 miljoner invånare. Att mäta virusmängder i avloppsvatten kan var en del av ett system för att detektera och övervaka förekomsten av SARS-CoV-2 i samhället. Notera att direkt jämförelse av virusmängden mellan olika städer inte är möjlig pga olika hantering av insamlade avloppsprov och analys av data.  Jämförelser bör endast göras inom data som samlats in och visualiseras från en och samma stad. [För mer information om epidemiologiska data från mätningar av SARS-CoV-2 i avloppsvatten se nedan](#background).

## Map of sample collection sites

<div class="row justify-content-center mb-4"><div class="col">{{< wastewater_map >}}</div></div>

## Uppsala, Umeå, Örebro, Kalmar, and other municipalities

This project is led by associate professor Anna J. Székely (SLU, Swedish University of Agricultural Sciences) and associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences). The project is made possible thanks to collaborations with Uppsala Vatten, Roslagsvatten, Enköpings kommun, Gästrike Vatten, TEMAB, and others.

The amount of SARS-CoV-2 virus in the Uppsala wastewater is estimated by analyzing raw wastewater collected at Kungsängsverket, Uppsala Vatten’s main treatment facility. The wastewater treated at the facility is collected by two main wastewater collection channels and covers territory inhabited by approximately 180,000 people. Please [consult this map for the exact catchment area of the two wastewater collection channels in Uppsala](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf). The amount of SARS-CoV-2 virus in the wastewater from municipalities surrounding municipalities is collected from other wastewater treatment plants. In particular, the amount of SARS-CoV-2 virus in the wastewater of Ekerö is estimated based on samples from Ekebyhov wastewater treatment plant, that of Österåker is based on Margretelund wastewater treatment plant, and that of Vaxholm is based on Blynäs wastewater treatment plant. Please [consult this map for the exact catchment area of the wastewater collection channels in Umeå](/wastewater/map_umeaa.jpg). Please [consult this map for the exact catchment area of the wastewater collection channels in Örebro](/wastewater/map_orebro.pdf).

Measurements are taken weekly, by processing a representative sample collected over 24 hours (i.e. flow compensated sample). The SARS-CoV-2 virus content of the wastewater on the given day is normalized to the fecal matter content to avoid variation from flow differences and population fluctuation. The samples are processed according to standard methods. Briefly, the viral content of the samples is concentrated according to the modified electronegative filtration method ([method C, Ahmed and colleagues, 2020](https://doi.org/10.1016/j.scitotenv.2020.139960)), viral RNA is extracted using the RNeasy PowerMicrobiome kit (Qiagen) and the copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). The virus recovery efficiency of the process and the presence of potential inhibitors is monitored by adding to the samples bovine coronavirus (BCoV) as process surrogate virus. To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV) which is the most abundant RNA virus in human feces and serves as an estimator of human fecal content ([Symonds and colleagues, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

Note that the scores provided in the dataset and depicted in plots below are preliminary. The team is still conducting method efficiency checks that might slightly affect the final results.

**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file.](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv) Data available starting from week 38 of 2020; updated weekly.\
**Contact:** anna.szekely@slu.se and maja.malmberg@slu.se\
**How to cite:**
Székely, A. & Mohamed, N. Dataset of SARS-CoV-2 wastewater data from Uppsala, and neighbouring towns Knivsta, Enköping, Östhammar and Älvkarleby, Sweden. [https://doi.org/10.17044/scilifelab.14256317.v1](https://doi.org/10.17044/scilifelab.14256317.v1) (2021).

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>
<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

## Stockholm

This project, led by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology; zeynepcg@kth.se), is a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater, started in mid-April 2020, from Bromma, Henriksdal, and Käppala wastewater treatment plants (WWTP). These treatment plants receive wastewater from a population of approximately 360,000; 860,000 and 500,000, respectively. Please consult [this map for the exact catchment area of the wastewater collection channels in Käppala](/wastewater/map_Kappala.pdf) and [this map for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

After concentration, filtering, and preparation, the samples are analyzed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)). In some cases, the raw wastewater has been frozen at –20 degrees, and  concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues is based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. The study concluded that the double ultrafiltration method adapted by KTH has a significantly higher efficiency compared to single filtration and adsorption methods. For detailed information about the concentration method, see the publication.

See also [the page of the research group where summaries of data and preliminary conclusions are presented](https://www.kth.se/water/research/covid-1.979048).

**Download the data:** [Relative N gene normalized by PPMoV; Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Results are available (partially) starting from week 16 of 2020; updated weekly.

**How to cite:**
Cetecioglu Z G, Williams, C, Khatami, K, Atasoy, M, Nandy, P, Jafferali, M H, Birgersson, M. SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483) (2021).

<div class="alert alert-info">Last updated: <span id="last_modified_stockholm"></span></div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

<div class="row ml-0 mt-3"><b>Publications:</b></div><div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939
</div></div>

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](historic_orebro_umea).
- [Historic data for Stockholm;  Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](historic_stockholm)

## Bakgrund

Epidemiologiska undersökningar av avloppsvatten kan användas för att studera SARS-CoV-2-virus i avföringsprover från COVID-19-patienter med RT-qPCR (se till exempel [Wu et al, 2020](https://doi.org/10.1016/S2468-1253(20)30083-2)). Övervakning av virusnivåerna av SARS CoV-2 i avloppsvatten från samhällen kan därför ge en tidig indikation på sjukdomsprevalensen på befolkningsnivå, kallad avloppsvattenbaserad epidemiologi ([Corpuz et al, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Avloppsvattenbaserad epidemiologi studerar mängden virusgenom i avloppsvattnet, med RT-qPCR. Avloppsvatten av består spillvatten, dagvatten och kylvatten. Dagvatten kommr från hushåll och fastigheter exempelvis kök, toaletter och duschar. Det kan dock också inkludera vatten från exempel regnvatten och vatten från industriellt bruk). Prover tas regelbundet vid avloppsreningsanläggningar, vilket gör det möjligt att jämföra virusbelastningen över tid. Det har tidigare visats att mängden SARS CoV-2-virus i avloppsvatten kan ge en indikation på ökad smittspridning i befolkningen och även att trenden SARS-CoV-2 i avloppsvatten korrelerar med antal fall av COVID-19 och antal patienter som behöver vård (se [Peccia et al, 2020](https://doi.org/10.1038/s41587-020-0684-z)). Under COVID-19-pandemin har övervakning av nivån SARS CoV-2 i avloppsvatten blivit en vanligare metod att övervaka och förutsäga smittspridning.

Observera att graferna som presenteras inom sektionen baseras på preliminära och ännu inte fullständigt utvärderade data. Data som delas ska därför användas med försiktighet. Observera att eftersom olika metoder för insamling av avloppsprover och dataanalys används av olika forskningsprojekten som redovisas nedan(dvs för olika städer) är det inte möjligt jämföra virusmängen mellan projekten (dvs mellan städer). Jämförelser bör göras inom varje projekt (dvs. stad) eftersom metoden är densamma för alla mätningar. Mätningar av SARS CoV-2 i avloppsvatten bör främst ses en indikation på ökande smittspridning, tillsammans med andra datatyper som exempelvis antal positiva SARS CoV-2 test, antal patienter som behöver intensivvård etc och  bidra till kunskap om den regionala dynamiken i COVID-19-pandemi.

{{< ww_dates_modified >}}
