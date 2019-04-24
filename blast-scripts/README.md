Scripts to setup a basic BLAST setup on a Jupyter server
========================================================

Outline:
1. Start a GCE instance
2. Set up the instance, run Jupyter notebook server
3. Open your Jupyter notebook on colab.research.google and connect it to a
   local runtime (i.e.: your GCE instance)


## 2. Set up instance
1. [`setup-blast.sh`](setup-blast.sh): Installs latest version of BLAST.
1. [`setup-aux-tools.sh`](setup-aux-tools.sh): Installs some helpful tools to
   run BLAST efficiently.
1. [`get-queries.sh`](get-queries.sh): Get sample query sequences from GCP, installs in `/blast/queries/contigs`.
1. [`get-blastdbs.sh`](get-blastdbs.sh): Installs BLAST databases in `/blast/db`
1. [`setup-jupyter-on-gce.sh`](setup-jupyter-on-gce.sh): Set up and Jupyter server on your instance 

Full instructions to :
https://research.google.com/colaboratory/local-runtimes.html

## 3. ... Connect to your colab.research.google to your Jupyter notebook server

On your local machine, create an ssh tunnel, and then click on 'Connect to
local runtime' (top right of the page in colab.research.google).

### How to set up the ssh tunnel?
* `ssh $USER@IP -L 8888:localhost:8888`, or 
* `gcloud compute ssh --zone YOUR_ZONE YOUR_INSTANCE_NAME -- -L 8888:localhost:8888`    
    
https://research.google.com/colaboratory/local-runtimes.html

