# Task008-P01-DS-SpaceX-Falcon-20240409
Predict successful landing 

<div>
    <h1> <a id="Obj1">🎯Objectives</a></h1>  
    
SpaceX advertises Falcon 9 rocket launches on its website for 62 million dollars, whereas other providers charge upwards of 165 million dollars each. The cost savings stem from SpaceX's capability to reuse the first stage. We will develop a model to predict the successful landing of the first stage, which will help estimate the launch cost for a bidding proposal.
    
<p style = "font-family: Arial; font-size: 14px">Note: This project's dataset was created for pedagogical purposes and may not be indicative of Space X.</p>
<hr>

<ol>
    <li> Collect and make sure the data is in the correct format from an API.
    <li> Predict if the Falcon 9 first stage will land successfully.
    </ol>
</div>

**Crash**

![Crash](02_Image/crash_SpaceX.gif)

**Landing**

![Landing](02_Image/landing_1_SpaceX.gif)

<div class="alert alert-block alert-warning">
<img style="float: left" src="https://i.postimg.cc/kXz8cFqC/005-Img-Yellow-Notes-Draft-1-20220819.png" width="60">
<b style = "font-family: Arial; font-size: 16px">Note:</b><p style = "font-family:Verdana; font-size:14px">We must maintain objectivity when analyzing the data to gain valuable insights. This involves collecting, fact-checking, and challenging the data and other sources. Adopting a Genchi Genbutsu approach, which involves go-seeing for yourself or discussing with subject matter experts, allows us to delve into the data to gain firsthand understanding.</p>
    <p>Data should adhere to the <b>COV-FAST</b> principles: Clear, Objective, Valuable, Focused, Agile, Scientific, and Time-bound. Additionally, consider exploring alternative models such as logistic regression, random forest, neural networks, or others.</p>
</div>
    <h3>Framework and Methodologies</h3>
     A <b>methodology</b> offers <b>specific steps</b> for completing a project, while a <b>framework</b> provides broader guidance on tools, resources, and workflow processes. As an experienced Green Belt Lean Six Sigma professional, the methodology that I often use is DMAIC. I used PACE as a framework as I found it similar to <b>Knowledge Discovery in Databases (KDD)</b>. Both <b>PACE</b> and <b>KDD</b> aim to guide structured data projects. <b>PACE</b> specifically focuses on machine learning projects, whereas <b>KDD</b> covers a broader range of data discovery techniques.
     
<h3>Data Analysis PACE Steps:</h3>
   <ol style="font-family:Verdana; font-size:16px">
    <li><img style="float:left" src="https://i.imgur.com/gIne5bH.png" width="50"> Plan/Prepare - import the relevant libraries and data</li> 
    <blockquote>
    <ol>Align project with business needs, requirements and contraints. Select an approriate machine learning model based on the problem and business context. KDD: Selection, Data Wrangling (Pre-processing and Transformation).
    </ol>
    </blockquote>
        <li><img style="float:left" src="https://i.imgur.com/rb8V6X5.png" width="50">Analyze - Explarotary Data Analysis (EDA)</li>
    <blockquote>
    <ol> Understanding data for accurate predictions, focus on the response variable (what the model predicts) and leverage exploratory data analysis to uncover patterns and address irregularities. KDD: Data Mining.
     </ol>
    </blockquote>
    <li><img style="float:left" src="https://i.imgur.com/J4M3HKM.png" width="50">Construct - model </li>
    <blockquote>
    <ol>Construct and evaluate model. KDD: Evaluation.
     </ol>
    </blockquote>
    <li><img style="float:left" src="https://i.imgur.com/wpcEXQC.png" width="50">Execute - share</li>
    <blockquote>
    <ol>Interpret model and share the story. KDD: Communicate to stakeholders.
     </ol>
    </blockquote>

<h2>Table of Contents</h2>
    
<div class="alert alert-block alert-info" style="margin-top: 20px">

<ol>
    <li><a href="#Obj1">Objectives</a></li>
    <li><a href="#Plan">Plan - import the relevant libraries and data</a></li>
    <ul>
        <li><a href="#Sel">Selection</a></li>
        <li><a href="#WS">Web Scraping</a></li>
        <li><a href="#DW">Data Wrangling</a></li>        
    </ul>
    <li><a href="#EDA">Explarotary Data Analysis (EDA)</a></li>
    <ul>
        <li><a href="#SQL">Analysis with SQL</a></li>
        <li><a href="#EDA_1">Explarotary Data Analysis (EDA)</a></li>
        <li><a href="#Inter_chart">Interactive Chart</a></li>
        <li><a href="#Feat">Feature Engineering</a></li>
        <li><a href="#Fol">Interactive visual analytics with folium</a></li>
        <li><a href="#Inter">Interactive dashboard on Website</a></li>
    </ul>
    <li><a href="#Construct">Construct - model</a></li>
    <ul>
        <li><a href="#Log_Reg">Logistic Regression</a></li>
        <li><a href="#SVM">Support Vector Machine (SVM)</a></li>
        <li><a href="#Tree">Decision Tree</a></li>
        <li><a href="#KNN">K Nearest Neighbours (KNN)</a></li>
    </ul>
    <li><a href="#Ex">Execute - share</a></li>
    <ul>
        <li><a href="#Sum">Summary </a></li>
    </ul>
</ol>
</div>
