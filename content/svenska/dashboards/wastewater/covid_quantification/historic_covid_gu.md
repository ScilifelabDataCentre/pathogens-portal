---
title: Historiska data för SARS-COV-2 i avloppsvatten (GU)
plotly: true
aliases:
  - /sv/dashboards/wastewater/covid_quant_gu/historic_covid_gu/
---

Denna webbsida visar historiska epidemiologiska data relaterade till SARS-CoV-2 i Göteborg, Sverige. Data har insamlats av Professor Helene Norders forskargrupp vid Göteborgs universitet, i samarbete med andra medarbetare från Göteborgs universitet och Sahlgrenska universitetssjukhuset (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). Data som visas på denna sida samlades in mellan vecka 7 2020 och vecka 42 2023 (dvs mellan 10 februari 2020 och 23 oktober 2023). Forskargruppen började under vecka 20 2023 att använda en ny metod för att studera SARS-CoV-2. Data som produceras med denna nya metod fortsätter att uppdateras ungefär en gång i veckan och är tillgängliga på webbsidan ['Mängd SARS-COV-2 i avloppsvatten (GU)'](/sv/dashboards/wastewater/covid_quantification/covid_quant_gu/).

## Insamlingsplatser för avloppsvatten

Ingående avloppsvattenprover insamlas från Ryaverkets avloppsreningsverk (eng. wastewater treatment plant WWTP) i Göteborg. Insamling av avloppsvattenprov startade 10 februari 2020 (vecka 7). Ryaverkets avloppsreningsverk samlar in avloppsvatten från mer än 790,000 invånare samt även från närliggande industrier. Avloppsvatten samlas även in från invånare och industrier inom närliggande områden som exempelvis Ale, Härryda, Kungälv, Lerum, Mölndal och Partille, samt från smältvatten från äldre delar av Göteborg. Mängd avloppsvatten från hushåll ligger på samma nivå över året, men den totala mängden avloppsvatten kan variera över året beroende på väderlek (högre luftfuktighet ger större mängd avloppsvatten). För mer information om uppsamling av avloppsvatten, veckor, volym avloppsvatten och flöde se [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: 2023-11-17</span></div>

_Det blå blocket på grafen indikerar den period då provtagningen gjordes inte (vecka 45 2022 - vecka 2 2023)._

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_gothenburg.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/gothenburg_covid_historic.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> 2023-11-07<br><b>Commentary:</b>There are still low amounts of SARS-CoV-2 in Gothenburg's wastewater. However, there was a small increase in weeks 41, 42, and 43 but there are still low levels.</div>

## Dataset

**Kontakt:** <helene.norder@gu.se>

**Nedladdning av data:** [Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://github.com/ScilifelabDataCentre/pathogens-portal/raw/develop/static/ww_data_temp/wastewater_data_gu_allviruses_historic.xlsx). Resultat finns tillgängliga för mängd SARS-CoV-2 från vecka 7 2020 (ett mindre uppehåll under vintern 2022-2023) , och för enterovirus från vecka 2 2023. Data uppdateras veckovis.

**För att citera datasetet:** Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

**För att citera metoden som används:**
Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Metoder

Insamling av avloppsvatten sker genom en fast insamlare som samlar in 30ml avloppsvatten per 10,000m<sup>3</sup>  av inkommande avloppsvatten. För analys veckovis poolas sju prover (varje avloppsvattenprov representerar insamling under ett dygn). Veckoprovet består av 1.5-15l avloppsvatten (beroende av flödet) som skickas till Klinisk Mikrobiologi vid Sahlgrenska Universitetssjukhuset för analys. Analys sker på måndagen i veckan efter provinsamling.

På Klinisk Mikrobiologi, koncentreras virusmängd genom en metod utvecklad på laboratoriet till en volym av 2.5ml. Denna metod använder NanoCeram electropositive filter (Argonide, Florida, USA) för att koncentrera prover, följt av ultracentrifugering som sekundär metod för att koncentrera prover ([Saguti _et al._, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). Nukleinsyror extraherades därefter från ett 1ml koncentrerat prov med hjälp av QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Realtids-PCR (RT-qPCR) användes för att detektera den RNA-beroende RNA polymerase (RdRP) regionen på SARS-CoV-2. Alla körningar innehöll en positiv kontroll bestående av en seriellt utspädd plasmid (Eurofins Genomics, Ebersberg, Germany). Nukleasfritt vatten används som negativ kontroll. Ct-värden från qPCR användes för att kvantifiera mängd SARS-CoV-2 genom i provet. En detaljerad beskrivning av hur mängd SARS-CoV-2 beräknas finns i [Saguti _et al._ (2021)](https://pubmed.ncbi.nlm.nih.gov/33212338/). Den relativa virusmängden i avloppsvatten beräknades genom att dela mängd viralt genom i prover med mängd SARS-CoV-2 genom i ingående mängd avloppsvatten vecka 11 (mitten av mars) 2020. Prover från alla följande veckor har innehållit detekterbara SARS-CoV-2 genom.
