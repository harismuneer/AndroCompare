<a href="#">
  <div align="center">
    <img src="main-title.png" width='200'/>
  </div>
</a>

<h1 align="center">AndroCompare</h1>

<p align="center">
  AndroCompare is a tool which takes two Android Apps (.APK files), compares them on a variety of factors and saves the resulting differences and similarities in a database.
</p>

<p align="center">
<a href="https://github.com/harismuneer"><img alt="views" title="Github views" src="https://komarev.com/ghpvc/?username=harismuneer&style=flat-square" width="125"/></a>
  <a href="https://doi.org/10.5281/zenodo.2537126">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.2537126.svg" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg?style=flat-square&logo=appveyor" />
  </a>
  <a href="#">
    <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" />
  </a>
  <a href="https://www.github.com/harismuneer/AndroCompare/fork">
    <img src="https://img.shields.io/github/forks/harismuneer/AndroCompare.svg?style=social&label=Fork&maxAge=2592000" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&label=Contributions&colorA=red&colorB=black" />
  </a>
</p>

<hr>

## Description

This tool is extremely fast and can be used to do massive comparison of a large number of apps quickly. 
Two sample apps named app1.apk and app2.apk are provided. These apps have been compared and their results are saved in the database so that you can see how the results are organized.

Moreover if two apps have same package name but differ hugely in the number of permissions requested and the activities etc then there's a strong chance that one of them is repackaged. So, this tool can highlight the extra permissions/activities added to the repackaged version and consequently help in malware detection too.

In order to create a dataset of apps, we wrote another tool: [Android Apsp Scraper/Downloader](https://github.com/harismuneer/Android-Apps-Downloader)

For details regarding **citing/referencing** this tool for your research, check the 'Citation' section below.

## Features
It compares apps for differences in:
* permissions requested
* activities
* services
* broadcast receivers
* content providers
* apk size
* version name and code
* signing certificate

and saves the results in an organized way in a SQLite database. 


## Schema of Database
```
CREATE TABLE `APPS` (
	`app1_name`	TEXT,
	`app2_name`	TEXT,
	`app1_package`	TEXT,
	`app2_package`	TEXT,
	`app1_size`	TEXT,
	`app2_size`	TEXT,
	`app1_version_name`	TEXT,
	`app2_version_name`	TEXT,
	`app1_version_code`	TEXT,
	`app2_version_code`	TEXT,
	`perm_analysis`	TEXT,
	`perm_same`	TEXT,
	`perm_added`	TEXT,
	`perm_removed`	TEXT,
	`perm_add_count`	TEXT,
	`app1_cert`	TEXT,
	`app2_cert`	TEXT,
	`cert_diff`	TEXT,
	`app1_main_activity`	TEXT,
	`app2_main_activity`	TEXT,
	`main_activity_diff`	TEXT,
	`same_activities`	TEXT,
	`activities_added`	TEXT,
	`activities_removed`	TEXT,
	`same_services`	TEXT,
	`services_added`	TEXT,
	`services_removed`	TEXT,
	`same_receivers`	TEXT,
	`receivers_added`	TEXT,
	`receivers_removed`	TEXT,
	`same_providers`	TEXT,
	`providers_added`	TEXT,
	`providers_removed`	TEXT
);
```

----------------------------------------------------------------------------------------------------------------------------------------
## How to Run 
In the code file 'andro_compare.py', change the path variables to the apps to be compared: 
```
# change the paths to the relevant apps to be compared
apk1_path = "./app1.apk"
apk2_path = "./app2.apk"
```

Its written in Python 2.6 and currently supports Linux only. Moreover it uses the "hurry.filesize" module. So, install it using the following command

```pip install hurry.filesize```

You can use [DB Browser for SQLite](http://sqlitebrowser.org/) to view the database.


## Note
This tool is for research purposes only.

----------------------------------------------------------------------------------------------------------------------------------------

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2537126.svg)](https://doi.org/10.5281/zenodo.2537126)

If you use this tool for your research, then kindly cite it. Click the above badge for more information regarding the complete citation for this tool and diffferent citation formats like IEEE, APA etc.

----------------------------------------------------------------------------------------------------------------------------------------

<br>
<hr>
<h1 align="left">Hey there, I'm <a href="https://www.linkedin.com/in/harismuneer/">Haris </a><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"> 
 <a href="https://github.com/harismuneer/Ultimate-Facebook-Scraper"><img align="right" src="https://user-images.githubusercontent.com/30947706/79588950-17515780-80ee-11ea-8f66-e26da49fa052.png" alt="Ultimate Facebook Scraper (UFS)" width="200"/></a> - Maker of Things</h1> 


### Creator of <a href="https://github.com/harismuneer/Ultimate-Facebook-Scraper">Ultimate Facebook Scraper</a> (one of the best software to collect Facebook data for research & analysis) 

<hr>

<h2 align="left">🌐 Connect</h2>
<p align="left">
  <a href="https://www.linkedin.com/in/harismuneer/"><img title="Follow on LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.facebook.com/harism99"><img title="Connect on Facebook" src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/></a>
  <a href="https://twitter.com/harismuneer99"><img title="Follow on Twitter" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
  <a href="mailto:haris.muneer5@gmail.com"><img title="Email" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://github.com/harismuneer"><img title="Follow on GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://www.instagram.com/harismuneer99"><img title="Follow on Instagram" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://www.youtube.com/channel/UCZ-uBd7g0E2Bp-0tXtSlSjw?sub_confirmation=1"><img title="Subscribe on YouTube" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/></a>
</p>


## 🤝 Consulting / Coaching
Stuck with some problem? Need help in solution development, guidance, training or capacity building? I am a Full Stack Engineer turned Project Manager with years of technical and leadership experience in a diverse range of technologies and domains. Let me know what problem you are facing at <b>haris.muneer5@gmail.com</b> and we can schedule a consultation meeting to help you get through it.

## 👨‍💻 Technical Skills & Expertise

- Development of Web Applications, Mobile Applications, and Desktop Applications
- Development of Machine Learning/Deep Learning models, and deployment 
- Web Scraping, Browser Automation, Python Scripting
<hr>



## ❤️ Support / Donations
If you or your company use any of my projects, like what I’m doing or have benefited from my projects in any way then kindly consider backing my efforts.

For donations, you can follow these simple steps:

<b>1)</b> Free signup at <b>[TransferWise](https://transferwise.com/invite/u/harism95)</b> using this link: https://transferwise.com/invite/u/harism95</li>. (Signing up through this link will save you from any transcation fee on the donation)

<b>2)</b> Select the amount e.g (15$) and choose the receiving/recipient's currency to be PKR. It supports multiple payment options (credit card, debit card, wire transfer etc)

<b>3)</b> Then it will show my info as the recipient, select it. If my name isn't shown, then type my email haris.muneer5@gmail.com in recipients.

<b>4)</b> Choose the reason for transfer to the one that suits you the most (in this case it could be 'General expenses') and in the reference section, you can mention 'Support'
 
If you face any issue in sending donation then feel free to get in touch with me at haris.muneer5@gmail.com 

Thank you for your contribution!



## Authors
You can get in touch with us on our LinkedIn profiles:


#### Haris Muneer

[![LinkedIn Link](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=linkedin&longCache=true&style=social&label=Follow)](https://www.linkedin.com/in/harismuneer) 

To stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/harismuneer)

#### Hussam Habib

[![LinkedIn Link](https://img.shields.io/badge/Connect-hussam--habib-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect)](https://www.linkedin.com/in/hussam-habib-0bb098104/)

To stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-hussam--habib-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/hussamh10)



---
If you liked the repo then kindly support it by giving it a star ⭐ and share in your circles so more people can benefit from the effort.

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

## Issues
[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/AndroCompare.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/harismuneer/AndroCompare/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](../master/LICENSE)

Copyright (c) 2018-present, harismuneer, hussamh10                                                        

