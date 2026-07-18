template = r"""
% !TeX spellcheck = en_GB
% !TeX program = pdflatex
%
% LuxSleek-CV 1.1 LaTeX template
% Author: Andreï V. Kostyrka, University of Luxembourg
%
% 1.1: added tracking and letter-spacing for prettier lower caps, added `~` for language levels
% 1.0: initial release
%
% This template fills the gap in the available variety of templates
% by proposing something that is not a custom class, not using any
% hard-coded settings deeply hidden in style files, and provides
% a handful of custom command definitions that are as transparent as it gets.
% Developed at the University of Luxembourg.
%
% *NOTHING IS HARCODED, and never should be.*
%
% Target audience: applicants in the IT industry, or business in general
%
% The main strength of this template is, it explicitly showcases how
% to break the flow of text to achieve the most flexible right alignment
% of dates for multiple configurations.

\documentclass[11pt, a4paper]{article} 

\usepackage[T1]{fontenc}     % We are using pdfLaTeX,
\usepackage[utf8]{inputenc}  % hence this preparation
\usepackage[british]{babel}  
\usepackage[left = 0mm, right = 0mm, top = 0mm, bottom = 0mm]{geometry}
\usepackage[stretch = 25, shrink = 25, tracking=true, letterspace=30]{microtype}  
\usepackage{graphicx}        % To insert pictures
\usepackage{xcolor}          % To add colour to the document
\usepackage{marvosym}        % Provides icons for the contact details
\usepackage{longtable}
%\usepackage[margin=1in]{geometry}
\usepackage{enumitem}        % To redefine spacing in lists
\setlist{parsep = 0pt, topsep = 0pt, partopsep = 1pt, itemsep = 1pt, leftmargin = 6mm}

\usepackage{sourcesanspro}        % Change this to use any font, but keep it simple
\renewcommand{\familydefault}{\sfdefault}

\definecolor{cvblue}{HTML}{304263}

%%%%%%% USER COMMAND DEFINITIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%
% These are the real workhorses of this template
\newcommand{\dates}[1]{\hfill\mbox{\textbf{#1}}} % Bold stuff that doesn’t got broken into lines
\newcommand{\is}{\par\vskip.5ex plus .4ex} % Item spacing
\newcommand{\smaller}[1]{{\small$\diamond$\ #1}}
\newcommand{\headleft}[1]{\vspace*{3ex}\textsc{\textbf{#1}}\par%
    \vspace*{-1.5ex}\hrulefill\par\vspace*{0.7ex}}
\newcommand{\headright}[1]{\vspace*{2.5ex}\textsc{\Large\color{cvblue}#1}\par%
     \vspace*{-2ex}{\color{cvblue}\hrulefill}\par}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage[colorlinks = true, urlcolor = white, linkcolor = white]{hyperref}
%\usepackage[sfdefault]{FiraSans}
\begin{document}

% Style definitions -- killing the unnecessary space and adding the skips explicitly
\setlength{\topskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\fboxsep}{0pt}
\pagestyle{empty}
\raggedbottom

\begin{minipage}[t]{0.33\textwidth} %% Left column -- outer definition
%  Left column -- top dark rectangle
\colorbox{cvblue}{\begin{minipage}[t][5mm][t]{\textwidth}\null\hfill\null\end{minipage}}

\vspace{-.2ex} % Eliminates the small gap
\colorbox{cvblue!90}{\color{white}  %% LEFT BOX
\kern0.09\textwidth\relax% Left margin provided explicitly
\begin{minipage}[t][293mm][t]{0.82\textwidth}
\raggedright
\vspace*{2.5ex}

\Large Vishvajit  \textbf{\textsc{Jambuti}} \normalsize 

% Centering without extra vertical spacing
\null\hfill\includegraphics[width=0.65\textwidth]{__IMAGE_PATH__}\hfill\null

\vspace*{0.5ex} % Extra space after the picture

\headleft{Profile}
{__PROFILE_DETAILS__}


\headleft{Contact details}
\small % To fit more content
\MVAt\ {\small vishvajitjambuti003@gmail.com} \\[0.4ex]
%\MVAt\ {\small Vishvajit.Jambuti@bertrandt.com} \\[0.4ex]
\Mobilefone\ +4917666070455 \\[0.5ex]
%\Mundus\ \href{https://github.com/WillyWonka}{github.com/WillyWonka} \\[0.1ex]
\Letter\ Ettinger Straße 1, \\85057  Ingolstadt 

\normalsize

\headleft{Personal info \& Language}
Birth Date : \dates{15/10/1993} \\[0.5ex]
English : \dates{C1} \\[0.5ex]
German : \dates{B2} \\[0.5ex]


\end{minipage}%
\kern0.09\textwidth\relax%%Right margin provided explicitly to stretch the colourbox
}
\end{minipage}% Right column
\hskip2.5em% Left margin for the white area
\begin{minipage}[t]{0.56\textwidth}
\setlength{\parskip}{0.8ex}% Adds spaces between paragraphs; use \\ to add new lines without this space. Shrink this amount to fit more data vertically

\vspace{2ex}

\headright{Experience}

{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf{Development Engineer}}}  \\
\hspace*{1em}\textit{Bertrandt AG (Ingolstadt).}\hfill\dates{01/2024 - Heute.}\
{__JOB_1_DETAILS__}

\is % Item spacing -- defined in the preamble
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Master's Thesis}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{08/2022 - 05/2023}\
\begin{itemize}
    \item Developed a real-time object detection system for construction site safety using YOLOv5 and PyTorch to detect personnel and construction equipment.
    \item Trained and optimized deep learning models on a GPU cluster, improving detection accuracy and inference performance.
    \item Deployed the object detection pipeline on an NVIDIA Jetson Nano and accelerated inference using TensorRT for edge AI applications.
    \item Designed and implemented ROS2-based image processing and sensor data pipelines for real-time perception and data integration.
    \item Containerized the complete application with Docker, enabling reproducible deployment, simplified maintenance, and portable edge-device execution.
\end{itemize}



\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Work student}}} \\
\hspace*{1em}\textit{Elvinci.de GmbH}\hfill\dates{04/2021 - 08/2022}\
{__JOB_2_DETAILS__}


\end{minipage}


\begin{minipage}[t]{0.33\textwidth} %% Left column -- outer definition
%  Left column -- top dark rectangle
\colorbox{cvblue}{\begin{minipage}[t][5mm][t]{\textwidth}\null\hfill\null\end{minipage}}

\vspace{-.2ex} % Eliminates the small gap
\colorbox{cvblue!90}{\color{white}  %% LEFT BOX
\kern0.09\textwidth\relax% Left margin provided explicitly
\begin{minipage}[t][293mm][t]{0.82\textwidth}
\raggedright
\vspace*{2.5ex}



\vspace*{0.5ex} % Extra space after the picture




\headleft{Skills}
\begin{itemize}
\item Python, C++,   C\# TypeScript, Matlab, SQL, Bash, 
\item Git, Jira, Docker, 
\item FastAPI, .NET, React, 
\item Vector, CANoe, CAPL
\end{itemize} 

\headleft{ \textcolor{cvblue!90}{key words}}
{__KEYWORDS__}


\end{minipage}%
\kern0.09\textwidth\relax%%Right margin provided explicitly to stretch the colourbox
}
\end{minipage}% Right column
\hskip2.5em% Left margin for the white area
\begin{minipage}[t]{0.56\textwidth}
\setlength{\parskip}{0.8ex}% Adds spaces between paragraphs; use \\ to add new lines without this space. Shrink this amount to fit more data vertically

\vspace{2ex}
\end{minipage}
\begin{minipage}[t]{0.56\textwidth}
\setlength{\parskip}{0.8ex}% Adds spaces between paragraphs; use \\ to add new lines without this space. Shrink this amount to fit more data vertically

\vspace{2ex}
\headright{Experience}
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Internship}}} \\
\hspace*{1em}\textit{Elvinci.de GmbH}\hfill\dates{11/2021 - 04/2021}\
\begin{itemize}
    \item Automated daily operational tasks to improve efficiency and streamline business processes.
    \item Performed statistical and predictive analysis of B2B sales data sourced from an ERP system.
    \item Designed and executed API test cases throughout the development lifecycle to identify issues early and improve overall API quality.
    \item Developed a mobile Android application for warehouse product data collection using Flutter and Dart.
    \item Created and executed test cases for the Android application to ensure functionality and reliability.
    \item Worked on  a product Recommendation  and Classification system.
\end{itemize}
\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Research Assistant RPTU}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{08/2019 - 10/2020}\

\begin{itemize}
    \item Developed a virtual 3D environment for production automation using Unreal Engine 4 and Blender.
    \item Created datasets for deep learning applications.
    \item Performed testing and validation of the generated datasets.
\end{itemize}

\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Project Work}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{11/2018 - 08/2019}\

\begin{itemize}
    \item Topic: Scene Matching
    \item Developed a virtual 3D environment in Unreal Engine 4 and conducted tests using real images.
    \item Tools and Frameworks Used: Finroc (Robotic Framework used in RR Lab TU KL), Unreal Engine 4, Blender
\end{itemize}

\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Electromobility Project}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{04/2017 - 06/2017}\
\begin{itemize}
    \item Performed energy consumption and energy management simulations for hybrid vehicles using MATLAB/Simulink.
\end{itemize}

\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Junior Engineer}}} \\
\hspace*{1em}\textit{Nirmiti Design Engineers PVT. LTD}\hfill\dates{07/2015 - 06/2016}\

\begin{itemize}
    \item Verified manufacturing work against CAD designs as a Junior Engineer.
    \item Conducted inventory reconciliation to ensure accurate inventory records.
    \item Coordinated material flow within the production process to ensure smooth manufacturing operations.
\end{itemize}

\headright{Education}
{\fontsize{12pt}{12pt}\selectfont
\textcolor{cvblue!90}{\textbf {M.Sc. in Commercial Vehicle Technology }}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{10/2016 - 04/2023}\\
\smaller{Thesis title: \textit{Optimization of Object Detection Models and Deployment on Edge Devices }} \\
\smaller{Focus Areas: Software Development, Robotics, Machine Learning, Electromobility, Simulation, Communication Protocols} \\

\is
{\fontsize{12pt}{12pt}\selectfont
\textcolor{cvblue!90}{\textbf {Bachelor of Enginnering in Maschinenbau }}} \\
\hspace*{1em}\textit{Pune University (India)}\hfill\dates{06/2011 - 06/2015}\\
\smaller{Focus Areas: Simulation, MMathematics, Mechanics, Thermodynamics, CAD/CAM, Manufacturing Technologies } \\




\end{minipage}

\end{document}

"""