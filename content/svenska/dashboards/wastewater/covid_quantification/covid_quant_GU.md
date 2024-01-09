---
title: Mängd SARS-COV-2 i avloppsvatten (GU)
plotly: true
aliases:
  - /sv/dashboards/wastewater/covid_quant_gu/
---

<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
<br>

## Introduktion

Denna webbsida visar historiska enteriska virusdata relaterade till SARS-CoV-2 i Göteborg, Sverige. Data har insamlats av Helene Norders forskargrupp vid Göteborgs universitet, i samarbete med andra medarbetare från Göteborgs universitet och Sahlgrenska universitetssjukhuset (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström), och Lucica Enache at Ryaverket, Gryaab AB, Gothenburg. Data som visas på denna sida samlades in mellan vecka 2 och vecka 42 2023 (dvs mellan 9 januari och 23 oktober 2023) vid Ryaverket. Forskargruppen började under vecka 20 2023 att använda en ny metod för att studera SARS-CoV-2. Alla forskningsdata som använder den nya metoden finns tillgängliga här ['historiska mängd SARS-COV-2 i avloppsvatten (GU)' page](/sv/dashboards/wastewater/covid_quantification/historic_covid_gu/) och data uppdateras ungefär **en gång per vecka**.

## Insamlingsplatser för avloppsvatten

Ingående avloppsvattenprover insamlas från Ryaverkets avloppsreningsverk (eng. waste water plant WWTP) i Göteborg. Insamling av avloppsvattenprov startade 10 februari 2020 (vecka 7). Ryaverkets avloppsreningsverk samlar in avloppsvatten från mer än 790,000 invånare samt även från närliggande industrier. Avloppsvatten samlas även in från invånare och industrier inom närliggande områden som exempelvis Ale, Härryda, Kungälv, Lerum, Mölndal och Partille, samt från smältvatten från äldre delar av Göteborg. Mängd avloppsvatten från hushåll ligger på samma nivå över året, men den totala mängden avloppsvatten kan variera över året beroende på väderlek (högre luftfuktighet ger större mängd avloppsvatten). För mer information om uppsamling av avloppsvatten, veckor, volym avloppsvatten och flöde se [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_gu"></span></div>

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_gothenburg.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/gothenburg_covid.py).

## Kommentarer från forskargruppen

<div><b>Date: <span id="gu_comment_date"></span></b> <br><b>Commentary:</b> <span id="gu_comment"></span></div>

{{< ww_dynamic_content >}}

## Dataset

**Kontakt:** <helene.norder@gu.se>

**Nedladdning av data:** [Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://github.com/ScilifelabDataCentre/covid-portal/raw/develop/static/ww_data_temp/wastewater_data_gu_allviruses.xlsx). Resultat finns tillgängliga för mängd SARS-CoV-2 från vecka 7 2020 (ett mindre uppehåll under vintern 2022-2023) , och för enterovirus från vecka 2 2023. Data uppdateras veckovis.\

**För att citera datasetet:** Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

**För att citera metoden som används:**
Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Metoder

Insamling av avloppsvatten sker genom en fast insamlare som samlar in 30ml avlopps vatten per 10,000m3 av inkommande avloppsvatten. För analys veckovis poolas sju prover (varje avloppsvatten prov representerar insamling under ett dygn). Veckoprovet består av 1.5-15l avloppsvatten (beroende av flödet) som skickas till Klinisk Mikrobiologi vid Sahlgrenska Universitetssjukhuset för analys. Analys sker på måndagen i veckan efter provinsamling.

Nukleinsyror extraheras från ett koncentrerat prov på 1 ml med hjälp av QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Realtids- PCR (RT-qPCR) användes för att detektera och kvantifiera mängd virusgenom. Mer information om metoden som används för att beräkna virusmängd finns i [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti _et al._ (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Wang _et al._ (2022)](https://doi.org/10.1016/j.isci.2022.105000), och [Wang _et al._ (2023)](https://doi.org/10.1016/j.scitotenv.2023.165012). Båda metoderna anges virusmängd per dag som ett genomsnitt, eftersom virusmängden baseras på en veckas insamling av avloppsvatten.

På Klinisk Mikrobiologi på Sahlgrenska Universitetssjukhuset används två metoder utvecklade inom gruppen för att koncentrera virusmängderna. Den metod som nu används använder sig av ultrafiltrering som primär metod. Den metod som tidigare användes använde ett elektropositivt filter (Argonide, Florida, USA) för att koncentrera proverna ([Saguti _et al._, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). Båda metoderna användes parallellt mellan vecka 20 och vecka 42 2023. All information som relateras till data insamlat med den tidigare används metoden finns på webbsidan för ['Historic SARS-CoV-2 data from Gothenburg' page](../).

Realtids-PCR (RT-qPCR) användes för att detektera den RNA-beroende RNA polymerase (RdRP) regionen på SARS-CoV-2. Alla körningar innehöll en positiv kontroll bestående av en seriellt utspädd plasmid (Eurofins Genomics, Ebersberg, Germany). Nukleasfritt vatten används som negativ kontroll. Ct-värden från qPCR användes för att kvantifiera mängd SARS-CoV-2 genom i provet. En detaljerad beskrivning av hur mängd SARS-CoV-2 beräknas finns i [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti _et al._ (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Wang _et al._ (2022)](https://doi.org/10.1016/j.isci.2022.105000), och [Wang _et al._ (2023)](https://doi.org/10.1016/j.scitotenv.2023.165012). I den tidigare använda metoden, som används tom vecka 42 223, beräknades den relativa virusmängden i avloppsvatten genom att dela mängd viralt genom i prover med mängd SARS-CoV-2 genom i ingående mängd avloppsvatten som detekterades i vecka 11 (mitten av mars) 2020. Prover från alla följande veckor har innehållit detekterbara mängder SARS-CoV-2 virus. (Se webbsidan för “Historic SARS-CoV-2 data from Gothenburg” ).Med den nya metoden, som används för de data som visas på denna webbsida, visas mängd virusgenom som ett genomsnitt baserat på en veckas insamlad mängd avloppsvatten.

<br>
<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
