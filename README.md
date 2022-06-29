# Web PAAS

A simple app to host stactic webcontent and provision Virtual Machines on AWS.

## 🚩 ABSTRACT

This Flask App helps in deploying static webpages by storing the content on AWS S3 bucket. It also has the facility to provision t2.micro/t3.micro EC2 instance on the AWS cloud. All of this is done with the help of automation API from  pulumi, an open source  infrastructure as code SDK.<br>

The website is created using HTML, CSS and Bootstrap along with Jinja2 Templating offered by Flask.

## 🌏 Web Pages

### Static Sites
This page show's a list of all the sites currently deployed. These are  ones that have already been created.
We can also create a new site where you can put in the name, and then put in a URL (where the HTML code is present), or type in your own HTML. When we click Create, it will deploy the site at AWS S3. The viewing console is a link to the public URL where the website is being hosted.

### Virtual Machines
To create a virtual machine choose an instance type. With the virtual machine, you're always gonna have a public key. If you don't have one, pulumi will handle it for you. This way it can be authenticated. After the virtual machine has been deployed the AWS, we can SSH into that, but we need to authenticate it with our private key. 

So right from this web interface, we'll be able to create, deploy and delete the virtual machine on AWS without actually going to our AWS dashboard. 


## 💻 Get Started

`!!! Ensure that you have an AWS, Pulumi account and aws-cli installed. !!!` <br>

```console
$ git clone https://github.com/Neelaksh-Singh/Web_PaaS.git
$ cd Web_PaaS/
```
Run `aws configure` and set your aws access key id and secret access key in the pwd.

To set pulumi project, create a pulumi account and run 
```console
> pulumi new
> select aws-python and give your project a name
>  Leave everything as is
```
Next we install all the required files. Activate your newly created Virtual Environment.( I'll be using Windows).

```console
$ venv\Scripts\activate.bat
$ pip install -r requirements.txt
```
Next we will generate ssh-key for our private key. This helps us in getting authenticated and unables to access the VM from our terminal. 
```console
> ssh-keygen -m PEM
Press enter for file and then enter passphrase of your choice. Go to the directory where you have saved the file and rename as following :=
> mv id_rsa id_rsa.pem
```
Make sure that the path is in your home directory.

Now You are all set to run your app. Just run `flask run` and you are good to go 👌. 
