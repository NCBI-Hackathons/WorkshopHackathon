Scripts to setup a basic BLAST setup on a Jupyter server
========================================================

Outline:
1. Start a GCE instance
2. Set up the instance, run Jupyter notebook server
3. Open your Jupyter notebook on colab.research.google and connect it to a
   local runtime (i.e.: your GCE instance)

# NOTE: 
If you're trying to run your jupyter notebook on a pre-configured server,
please follow the instructions on step 3.


## 2. Set up instance
1. [`setup-blast.sh`](setup-blast.sh): Installs latest version of BLAST.
1. [`setup-aux-tools.sh`](setup-aux-tools.sh): Installs some helpful tools to
   run BLAST efficiently.
1. [`get-queries.sh`](get-queries.sh): Get sample query sequences from GCP, installs in `/blast/queries/contigs`.
1. [`get-blastdbs.sh`](get-blastdbs.sh): Installs BLAST databases in `/blast/db`
1. [`setup-jupyter-on-gce.sh`](setup-jupyter-on-gce.sh): Set up and Jupyter server on your instance 
1. [`run-jupyter-on-gce.sh`](run-jupyter-on-gce.sh): Start jupyter server.

## 3. ... Connect your colab.research.google to your Jupyter notebook server

1. On your local machine, create an ssh tunnel:

    ```bash
    # Two possibilities:
    ssh $IP -L 8888:localhost:8888`   # OR  
    gcloud compute ssh --zone YOUR_ZONE YOUR_INSTANCE_NAME -- -L 8888:localhost:8888`    
    ```

1. Authenticate (this is only needed the first time you connect to a running jupyter server - may need to re-run if the server was restarted).
   1.1 Open your web browser in which your colab jupyter notebook is open and go to the authentication URL (will look like the URL below, this is the
       output of step 2.6). Ask the person who set up/started the jupyter notebook server for the actual URL

  http://localhost:8888/?token=6a79bffd168062a2254fa4731274d46730d13dee952478fc
    
1. Click on 'Connect to local runtime' (top right of the page in `colab.research.google`).


Full instructions: https://research.google.com/colaboratory/local-runtimes.html
