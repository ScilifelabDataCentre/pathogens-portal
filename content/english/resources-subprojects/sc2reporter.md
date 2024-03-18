---
title: "SARS-CoV-2 Reporter for visualisation of SARS-CoV-2 genome sequence data (SC2reporter)"
category: "plp1"
resource_info:
  name: "SARS-CoV-2 Reporter for visualisation of SARS-CoV-2 genome sequence data (SC2reporter)"
  funded_project_title: "Genomic Pandemic Preparedness Portfolio (G3P) (PLP1 capability)"
  pi: Jonas Björkman (Region Skåne)
  host_organisation: Multiple organisations contribute to SC2reporter;  Region Skåne (initial developer), Lund University, Karolinska Institutet, Karolinska University Hospital, GMS
  use: "This resource can be used to explore SARS-CoV-2 sequence data. The tool has multiple features:<br><ul><li>List all variants a single isolate contains. This includes nuc and aa changes over the complete genome including the coverage, frequency, and prevalence of the mutation in your own dataset.</li><li>Compare the isolate with all other isolates in your database within a set number of variant differences.</li><li>Show pango and nextstrain clades</li><li>Every mutation and type is hyperlinked to external resources for additional information</li><li>A dashboard that gives an overview of types over time</li><li>A rerun tool that helps evaluate reruns of isolates in the lab.</li><li>Visualise phylogenetic trees of selected isolates</li></ul><br>We are currently working on a new release where we will be:<br><br></ul><li>Separating the back end from the front end.</li><li>Rewriting the front end in React and back end to FastAPI</li><li>Adapt the database model and interface to be able to handle more virus types than SARS-CoV-2</li><li>Improving the functionality of the tree drawing and its algorithms</li><li>Restructuring the database schema for faster handling</li></ul>"
  access: "SC2Reporter is available free-of-charge on [GitHub](https://github.com/genomic-medicine-sweden/sc2reporter)."
  data_etc: "All code related to SC2Reporter is available on [GitHub](https://github.com/genomic-medicine-sweden/sc2reporter)."
  publications_etc: "Instructions about how to use SC2Reporter and relevant reports are available on [GitHub](https://github.com/genomic-medicine-sweden/sc2reporter)."
  webpage: "[https://github.com/genomic-medicine-sweden/sc2reporter](https://github.com/genomic-medicine-sweden/sc2reporter)"
  contact: "Jonas Björkman<br>Molecular Biologist<br>Email: [Jonas.bjorkman@skane.se](mailto:Jonas.bjorkman@skane.se)"
---

A web-based visualisation application for the ongoing SARS-CoV-2 pandemic. The tool is primarily used for epidemiological analysis where pipeline analysis results and metadata are loaded into a mongoDB database. The SNVs and indels can then be compared between all isolated in the database.

For more information on the [Pandemic Laboratory Preparedness resources](/resources/) associated with this subproject, see [Genomic Pandemic Preparedness Portfolio (G3P)](/resources/g3p/). Please also refer to other associated subprojects; [GMS Arctic](/resources-subprojects/gms-arctic/) and [taxprofiler](/resources-subprojects/taxprofiler/).

Below is a still image of one of the visualisations produced using SC2reporter.

<figure class="figure">
  <img src="/resorces/reporter_pangograph.png" class="figure-img img-fluid" alt="A generic square placeholder image with rounded corners in a figure.">
  <figcaption class="figure-caption">Example visualisation from SC2reporter.</figcaption>
</figure>
