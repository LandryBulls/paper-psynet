# The neural representation of self is recapitulated in the brains of friends: a round-robin fMRI study.

This repository contains materials and analysis notebooks (in both Jupyter and R Markdown formats) to generate all resuls and figures from:

Chavez, R.S., Wagner, D.D. The neural representation of self is recapitulated in the brains of friends: a round-robin fMRI study.

The contents of this repository are also available on the Open Science Framework at [https://osf.io/ykspn/](https://osf.io/ykspn/). 

# Materials

(Psychopy)[http://www.psychopy.org/] scripts are provided for running the behavioral (**behavioral_ratings_task**) and neuroimaging (**fMRI_task**) components of this study. Real names of the targets that were used during the actualy study have been replaced with generic identifies (e.g. 'name1') to protect participants privacy. The tasks were administered using Psychopy v.1.83.04 running on a Lenovo Thinkpad.

# Analysis notebooks

Notebooks in both [R Markdown](https://rmarkdown.rstudio.com/) and [Jupyter](http://jupyter.org/) (using the R kernel) format are included for generating the results and figures from the manuscript based on the behavioral and neural datasets (i.e., **behaviroal_ratings.csv** and **fmri_vmpfc_betas**).

## Description of files

Datasets:
* behavioral_ratings.csv: Behavioral trait ratings for each target made by each participant.
* fmri\_vmpfc\_betas: Voxel coordinates and responses extracted from an independent VMPFC localizer. Each row represents one participant's voxel responses from the VMPFC to a given target. 

Notebooks:
* R Markdown: psynet.md
* R Notebook (and knit HTML file): psynet.np.html
* Jupyter Notebook (R kernel): psynet.ipynb









