---
title: Amount of SARS-CoV-2 in wastewater (GU)
toc: false
plotly: true
---

<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
<br>

## Introduktion

Detta projekt leds av professor Helene Norder (Göteborgs universitet, GU), i samarbete med  anställda vid Göteborgs universitet och Sahlgrenska Universitetssjukhuset (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti och Kristina Nyström). Avloppsvattenprover insamlas av Lucica Enache vid Ryaverkets avloppsreningsverk, Gryaab AB, Göteborg.

Data och visualiseringar på denna sida uppdateras veckovis.

## Insamlingsplatser för avloppsvatten

Ingående avloppsvattenprover insamlas från Ryaverkets avloppsreningsverk (eng. waste water plant WWTP) i Göteborg. Insamling av avloppsvattenprov startade 10 februari  2020 (vecka 7). Ryaverkets avloppsreningsverk samlar in avloppsvatten från mer än 790,000 invånare samt även från närliggande industrier. Avloppsvatten samlas även in från invånare och industrier inom närliggande områden som exempelvis Ale, Härryda, Kungälv, Lerum, Mölndal och Partille, samt från smältvatten från äldre delar av Göteborg. Mängd avloppsvatten från hushåll ligger på samma nivå över året, men den totala mängden avloppsvatten kan variera över året beroende på väderlek (högre luftfuktighet ger större mängd avloppsvatten). För mer information om uppsamling av avloppsvatten, veckor, volym avloppsvatten och flöde se [Wang *et al.* (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_gu"></span></div>

<!-- <button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  How to use the interactive features of the plot
</button>

 <div class="modal fade" id="interactiveFeaturesModal" tabindex="-1" aria-labelledby="interactiveFeaturesModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="interactiveFeaturesModalLabel">Information on how to use the interactive features of the plot</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>The line plots on this page have multiple interactive features. You can use the features to view the data in them in different ways. For example, you can choose to view data only within a certain time period, or from a given collection site. Below, we explain how to use different interactive features to meet your needs.</p>
        <h6>View data from particular sites</h6>
        <p>To view only data from a single site, double click on the name on that site in the legend to the right. To toggle data from a site on/off, single click on the name in the legend. If the data is 'deselected', the name will appear 'greyed out' in the legend, and it will not be displayed on the graph. Initially, all data will be 'selected'. To 'deselect' all data, use the 'Deselect all areas' button. You can use the 'Reselect all areas' button to 'select' data from every site (i.e. return to the default view).</p>
        <h6>View only certain y- and/or x-axes ranges</h6>
        <p>In the below plots, the y-axis represents the copy number of SARS-CoV-2 relative to PMMoV while the x-axis represents the date. If you would like to view values within a given range of the values on the axes, you can do this by clicking and dragging with your mouse. For example, to view all data within a given timeframe, you can click near the start date on the x-axis and drag to create a rectangle that encompasses the whole y-axis and the range of dates on the x-axis that you want to view. The plot will then zoom into the range that you selected.</p>
        <h6>Accurately read data values</h6>
        <p>It is difficult to accurately read the exact values of data from a graph. In order to view the exact data values, hover over the data point of interest. A box will appear that shows the y-axis values for all sites on that date (i.e. that x-axis value).</p>
        <h6>Other features</h6>
        <p>If you hover your cursor over the plot, you will see some additional options as grey icons in the top right. You can use these features to zoom in/out of the plot (using the + and - icons), and scale the axes so that the data from the 'selected' sites are shown on the most appropriate axes (this can be done using the autoscale or reset axes icons, which look like a box containing arrows and a house, respectively).</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div> -->

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_gothenburg.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/gothenburg_covid.py).

## Kommentarer från forskargruppen

<div><b>Datum:</b> <span id="gu_comment_date"></span><br><b>Kommentar:</b> <span id="gu_comment"></span></div>

{{< ww_dynamic_content >}}

## Dataset

**Kontakt:** helene.norder@gu.se

**Nedladdning av data:** [Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Resultat finns tillgängliga för mängd SARS-CoV-2 från vecka 7 2020 (ett mindre uppehåll  under vintern 2022-2023) , och för enterovirus från vecka 2 2023. Data uppdateras veckovis.\

**För att citera datasetet:**  Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

**För att citera metoden som används:**
Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Metoder

Insamling av avloppsvatten sker genom en fast insamlare som samlar in 30ml  avlopps vatten per 10,000m3  av inkommande avloppsvatten. För analys veckovis poolas sju prover (varje avloppsvatten prov representerar insamling under ett dygn). Veckoprovet består av 1.5-15l avloppsvatten (beroende av flödet) som skickas till Klinisk Mikrobiologi vid Sahlgrenska Universitetssjukhuset för analys. Analys sker på måndagen  i veckan efter provinsamling.

På Klinisk Mikrobiologi, koncentreras virusmängd genom en metod utvecklad på laboratoriet till en volym av 2.5ml. Denna metod använder NanoCeram electropositive filter (Argonide, Florida, USA) för att koncentrera prover, följt av ultracentrifugering som sekundär metod för att koncentrera prover ([Saguti *et al.*, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). Nukleinsyror extraherades därefter från ett 1ml koncentrerat prov med hjälp av QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Realtids-PCR (RT-qPCR) användes för att detektera den RNA-beroende RNA polymerase (RdRP) regionen på SARS-CoV-2. Alla körningar innehöll en positiv kontroll bestående av en seriellt utspädd plasmid (Eurofins Genomics, Ebersberg, Germany). Nukleasfritt vatten används som negativ kontroll. Ct-värden från qPCR användes för att kvantifiera mängd SARS-CoV-2 genom i provet. En detaljerad beskrivning av hur mängd SARS-CoV-2 beräknas finns i [Saguti *et al.* (2021)](https://pubmed.ncbi.nlm.nih.gov/33212338/). Den relativa virusmängden i avloppsvatten beräknades genom att dela mängd viralt genom i prover med mängd SARS-CoV-2 genom i ingående mängd avloppsvatten vecka 11 (mitten av mars) 2020. Prover från alla följande veckor har innehållit detekterbara SARS-CoV-2 genom.

<br>
<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
