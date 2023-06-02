---
title: CRUSH Covid data och dashboard, Region Uppsala
description: CRUSH Covid kartlägger smittspridningen av Covid-19 i Uppsala län genom visualiseringar av antal fall, testpositivitet och geografisk spridning. Data (postnummer) tillgängligt för nedladdning.
banner: /dashboard_thumbs/CRUSH.png
toc: false
aliases:
  - /sv/data_types/health_data/crush_covid/
menu:
  dashboard_menu:
    identifier: crush_covid
    name: CRUSH Covid Uppsala (Partnerprojekt)
---

<div class="containter">
<div class="row mr-2 mt-2">
<div class="col-lg-9">
<p>CRUSH Covid Uppsala är ett forskningsprojekt där <b>Region Uppsala</b> samarbetar med forskare från fem olika forskningsavdelningar vid <b>Uppsala universitet</b>. Syftet med projektet är att kartlägga utbrott av covid-19 i Uppsala län och att försöka mildra effekterna av utbrott genom att informera allmänheten.</p>

<p>CRUSH Covid leds av <b>Mats Martinell</b> (universitetslektor vid Institutionen för folkhälso-och vårdvetenskap, Allmänmedicin och Preventivmedicin, Uppsala universitet) och <b>Tove Fall</b> (professor vid Institutionen för medicinska vetenskaper, Molekylär epidemiologi, Uppsala universitet). Provtagningen på avloppsvatten stöds av SciLifeLab och Uppsala Vatten. Data modelleringen har anslag från Vinnova.</p>

<p>För frågor och feedback, kontakta <b>Elin Clauson</b> (<a href="mailto:elin.clauson@medsci.uu.se">elin.clauson@medsci.uu.se</a>).</p><p>CRUSH Covid har etiskt tillstånd från Etikprövningsmyndigheten (DNR 2020-04210, 2020-06315 och 2020-06501).</p>

<p>CRUSH Covid-teamet har släppt data och information om projektet på två ställen. Den primära källan till data och information var deras <a target="_blank" href="https://crush-covid.shinyapps.io/crush_covid/">anpassade shiny app, som heter CRUSH Covid-instrumentpanelen</a>, som innehöll datavisualiseringar samt rapporter. Från och med september 2022 upphörde uppdateringar av appen. Portalens instrumentpanel (dvs den här webbsidan) är den sekundära källan till data och information för detta projekt. Data som genereras från CRUSH Covid mellan 2020-2022 kan laddas ner direkt nedan.</p>
</div>
<div class="col-lg-3">
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/crush_covid_logo.png" alt="CRUSH Covid" height="30"></div>
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/uu_logo.png" alt="Uppsala University" height="100"></div>
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/regionuppsala_logo.png" alt="Region Uppsala" height="40"></div>
</div>
</div>
</div>

#### Ladda ner CRUSH Covid data

<div class="alert alert-info">Senast uppdaterad: 2022-09-15</div>

- [Antal test per capita och % positiva fall i varje postnummer i Uppsala län, .csv fil](https://blobserver.dc.scilifelab.se/blob/CRUSH_Covid_data.csv). För varje postnummer i Uppsala län, innehåller vår dataset datauppgifter om Covid-19 fall per capita, test per capita och % positiva fall. Våra uppskattningar beräknas utifrån den vuxna befolkningen i varje postnummer (personer 15 år och äldre). Som referens har både den totala befolkningen och den vuxna befolkningen inkluderats.

#### Dashboard med interaktiv grafik och veckorapport

<a target="_blank" href="https://crush-covid.shinyapps.io/crush_covid/">Klicka här</a> för att se interaktiv grafik och veckorapport i ett nytt fönster.

{{< crush_covid >}}
