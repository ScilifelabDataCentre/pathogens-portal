---
title: Large scale immunofluorescence to explore the host cell response to SARS-CoV-2 infection
date: 2022-04-08 # change later
summary:  Expression of 602 host proteins were evaluated in populations of infected and non-infected cells using immunofluorescence. ≈75,000 images have been published as a resource for further studies.
banner: /highlights/banners/immunofluorescence.png
banner_large: /highlights/banners/immunofluorescence.png
banner_caption: Part of Figure 2 from Kaimal, Tampere et al 2022; Representative images of proteins with reduced or increased intensity during SARS-CoV-2 infection. # change later
highlights_topics: [COVID-19, Infectious diseases]
imjoy:
    config:
        show_window_title: true
        # menu_container: "menu-container"
        menu_style: { float: 'right' }
    startup: |
        async function(){
            await api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-Classification.imjoy.html', window_id: 'sars-cov-2-infection-explorer', window_style: {height: '600px'}});
        }
---

Over the last two years, the COVID-19 pandemic has significantly affected people’s lives worldwide. Apart from vaccination to prevent COVID-19, there is a need to identify different treatment options for people already being infected and suffering from it. Further, general strategies for how to identify and develop effective drugs for any cause of possible future pandemics are needed.

The process of drug development, from identifying the compound to an approved drug is both long and costly. Therefore, drug repurposing – using already approved drugs for treatments of another condition, is a way to shorten this time frame. However, thousands of drugs are available, and it would not be practically possible to test them all for every new possible purpose. To make drug repurposing more effective and less resource demanding, a targeted approach could help determining which drugs are potentially usable.

One strategy that has been suggested to ‘narrow down’ the number of drugs for drug repurposing is based on identifying the host cell proteins that change location or abundance upon infection in situ using immunofluorescence. These proteins are considered to have a role in the viral replication life cycle and are thereby putative targets to treat infection. Once such proteins are identified, drugs that target those proteins could be applied in drug screening and evaluated for their effect on antiviral activity. This strategy was recently explored by researchers from KTH/SciLifeLab and Karolinska Institute/Scilifelab. In the [preprint recently released by the researchers](https://doi.org/10.1101/2022.03.29.482838) (first author: Jayasankar Mohanakrishnan Kaimal and Marianna Tampere, corresponding authors: Päivi Östling and Charlotte Stadler), they demonstrate that this strategy is feasible.

The researchers developed an assay for SARS-CoV-2 infection of Vero-E6 cells. Then, the subcellular localisation and expression of ≈ 600 host proteins were evaluated in mixed populations of infected and non-infected cells using immunofluorescence and antibodies from the [Human Protein Atlas (HPA)](https://www.proteinatlas.org/) project.

Among the 602 proteins, 97 were found to have an altered profile in infected cells. Of these, 45 were shown to have elevated abundance whilst 10 showed reduced abundance. Further, 20 proteins changed their localization within the cell when infected, and 22 proteins exhibited changed expression and localisation.

The host cell proteins identified in the assay were then considered as targets for a drug repurposing screen, using compounds from the SPECS repurposing library (Broad Institute). The team thus further optimized their host response screen to be compatible with drug repurposing in SARS-CoV-2 infected cells. In total, 116 drugs towards 21 of the identified host targets were available from the SPECS library and included in the repurposing screen. From the screen three compounds - elesclomol, crizotinib and rimcazole – were identified with significant antiviral activity and will be subjects for further validation studies.
In summary, the study demonstrates that immunofluorescence used to identify potential host targets, is an effective approach for more targeted drug repurposing. This could have significant impact in the future by enabling researchers to ‘narrow down’ the number of existing drugs that are likely to be useful for treatment, or to identify novel targets for drug discovery.

#### Preprint

DOI: [10.1101/2022.03.29.482838](https://doi.org/10.1101/2022.03.29.482838)

Jayasankar Mohanakrishnan Kaimal, Marianna Tampere, Trang H. Le,Ulrika Axelsson, Hao Xu, Hanna Axelsson, Anna Bäckström, Francesco Marabita, Elisabeth Moussaud-Lamodière, Duncan Njenda, Carolina Oses Sepulveda, Wei Oyuang, Brinton Seashore-Ludlow, Caroline Vernersson, Ali Mirazimi, Emma Lundberg, Päivi Östling, Charlotte Stadler. *bioRxiv* (2022; published on March 29, 2022).

#### Immunofluorescence images

The team has openly shared images ≈75,000 confocal images of SARS-CoV2 infected and non-infected Vero E6 cell populations under [DOI:10.17044/scilifelab.14315777](https://doi.org/10.17044/scilifelab.14315777):

> Cells had been infected with the virus for 1 h and fixed 24 hour post infection in 96 well plates. Using immunofluorescence (4 colours) cells were stained for the SARS-CoV2 virus (red), the endoplasmic reticulum (yellow) and nucleus (blue) – same for all images in the data set and used as reference markers. On top of this, 700 different target proteins were stained – one per well (green). Images were acquired with an Opera Phoenix microscope at 63X, using 9 FoV and 3 z-planes per protein target.

### Explore the images

Below, you can explore the immunofluorescence images using the Vizarr plugin for ImJoy. You can select a plate to view and adjust viewing options.

<div class="container">
  <div class="row">
    <div class="col-md-6">
      <select class="form-control" id="select_plate" onchange="change_plate()">
        <option value="p1">Plate 1</option>
        <option value="p2">Plate 2</option>
        <option value="p3">Plate 3</option>
        <option value="p4">Plate 4</option>
        <option value="p5">Plate 5</option>
        <option value="p6">Plate 6</option>
        <option value="p7">Plate 7</option>
      </select>
    </div>
  </div>
  <div class="row mt-3">
    <div id="explorer">You selected: p1</div>
  </div>
</div>



<!--
plate 1 offsets: https://scilifelab.figshare.com/ndownloader/files/27671955
plate 1 filenames: https://scilifelab.figshare.com/ndownloader/files/33894767
plate 1: https://scilifelab.figshare.com/ndownloader/files/27671958
plate 2 offsets: https://scilifelab.figshare.com/ndownloader/files/27672693
plate 2 filenames: https://scilifelab.figshare.com/ndownloader/files/33471335
plate 2: https://scilifelab.figshare.com/ndownloader/files/27672696
plate 3 offsets: https://scilifelab.figshare.com/ndownloader/files/27672879
plate 3 filenames: https://scilifelab.figshare.com/ndownloader/files/33471329
plate 3: https://scilifelab.figshare.com/ndownloader/files/27672903
plate 4 offsets: https://scilifelab.figshare.com/ndownloader/files/27673344
plate 4 filenames: https://scilifelab.figshare.com/ndownloader/files/33471326
plate 4: https://scilifelab.figshare.com/ndownloader/files/27673347
plate 5 offsets: https://scilifelab.figshare.com/ndownloader/files/27673614
plate 5 filenames: https://scilifelab.figshare.com/ndownloader/files/33471323
plate 5: https://scilifelab.figshare.com/ndownloader/files/27673620
plate 6 offsets: https://scilifelab.figshare.com/ndownloader/files/27674610
plate 6 filenames: https://scilifelab.figshare.com/ndownloader/files/33471320
plate 6: https://scilifelab.figshare.com/ndownloader/files/27686883
plate 7 offsets: https://scilifelab.figshare.com/ndownloader/files/27687051
plate 7 filenames: https://scilifelab.figshare.com/ndownloader/files/33471317
plate 7: https://scilifelab.figshare.com/ndownloader/files/27687054
-->

<script>
function change_plate() {
  var x = document.getElementById("select_plate").value;
  document.getElementById("explorer").innerHTML = "You selected: " + x;
}
</script>

<div id="sars-cov-2-infection-explorer"></div>
