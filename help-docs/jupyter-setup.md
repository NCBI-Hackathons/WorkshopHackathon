## Jupyter Setup Notes

* Start [Here](https://the-littlest-jupyterhub.readthedocs.io/en/latest/install/google.html).


* Run this manually as root

```bash
#!/bin/bash
curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py \
  | sudo python3 - \
    --admin [some-admin-username]
```
* Install any other software needed: pandas, conda, biopython, etc.

* Create a domain name pointing to your server

* SSL Setup

```bash
    $ sudo tljh-config set https.enabled true
    $ sudo tljh-config add-item https.letsencrypt.domains [domain.ext]
    $ sudo tljh-config set https.letsencrypt.email valid-email@example.com
    $ sudo tljh-config show
    $ sudo tljh-config reload proxy
```

* Oauth Github Setup

  * Set up the [GitHub OAuth Application]()
  
```bash
    $ sudo tljh-config set auth.GitHubOAuthenticator.client_id '[client_id]'
    $ sudo tljh-config set auth.GitHubOAuthenticator.client_secret '[client_secret]'
    $ sudo tljh-config set auth.GitHubOAuthenticator.oauth_callback_url 'https://[domain]/hub/oauth_callback'
    $ sudo tljh-config set auth.type oauthenticator.github.GitHubOAuthenticator

    $sudo tljh-config reload
```

> To allow any user use
> `tljh-config set auth.FirstUseAuthenticator.create_users true`
or
> `tljh-config set auth.GitHubOAuthenticator.create_users true`

> Note: Default GitHubOAuthenticator setup causes a 500 error on login due to Tornado version incompatibility.

> https://github.com/jupyterhub/the-littlest-jupyterhub/issues/289

> Fix:

```bash
$ sudo su -
# cd /opt/tljh/hub
# source ./bin/activate
# pip3 freeze | grep tornado
tornado==6.0.2
# pip3 install tornado==5.1.1
# pip3 freeze | grep tornado
tornado==5.1.1
# exit
$ sudo tljh-config reload proxy
$ sudo tljh-config reload
```



Generate nbgitpuller links to import github notebooks to tljh
https://mybinder.org/v2/gh/jupyterhub/nbgitpuller/master?urlpath=apps/binder%2Flink_generator.ipynb

