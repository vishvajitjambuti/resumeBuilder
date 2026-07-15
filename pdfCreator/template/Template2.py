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

\headleft{Personal info \& Sprache}
Birth Date : \dates{15/10/1993} \\[0.5ex]
English : \dates{C1} \\[0.5ex]
Deutsch : \dates{B2} \\[0.5ex]


\end{minipage}%
\kern0.09\textwidth\relax%%Right margin provided explicitly to stretch the colourbox
}
\end{minipage}% Right column
\hskip2.5em% Left margin for the white area
\begin{minipage}[t]{0.56\textwidth}
\setlength{\parskip}{0.8ex}% Adds spaces between paragraphs; use \\ to add new lines without this space. Shrink this amount to fit more data vertically

\vspace{2ex}

\headright{Erfahrung}

{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf{Entwicklungsingenieur}}}  \\
\hspace*{1em}\textit{Bertrandt AG (Ingolstadt).}\hfill\dates{01/2024 - Heute.}\
{__JOB_1_DETAILS__}

\is % Item spacing -- defined in the preamble
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Masterarbeit}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{08/2022 - 05/2023}\
\begin{itemize}
    \item Entwicklung eines Echtzeit-Objekterkennungssystems für die Baustellensicherheit mit YOLOv5 und PyTorch.
    \item Training und Optimierung von Deep-Learning-Modellen auf einem GPU-Cluster.
    \item Deployment auf einer NVIDIA Jetson Nano und Optimierung der Inferenz mit TensorRT.
    \item Entwicklung ROS2-basierter Bildverarbeitungs- und Sensordaten-Pipelines.
    \item Containerisierung der Anwendung mit Docker für eine reproduzierbare Bereitstellung.
\end{itemize}



\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Werkstudent}}} \\
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
\headright{Erfahrung}
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Praktikum}}} \\
\hspace*{1em}\textit{Elvinci.de GmbH}\hfill\dates{11/2021 - 04/2021}\
\begin{itemize}
    \item Automatisierung der täglichen betrieblichen Aufgaben. 
    \item  Durchführung statistischer und prädiktiver Analysen von B2B-Verkaufsdaten, die aus einem ERP-Tool stammen.
    \item Entwicklung und Durchführung von API-Testfällen während des Entwicklungszyklus, um Problemefrühzeitig zu erkennen und die allgemeine API-Qualität zu verbessern.
    \item Entwicklung einer mobilen Android-Anwendung für die Datenerfassung der Produkte im Lager (in flutter,dart), und Erstellung von Testfällen für die Android-App.
    \item Entwicklung eines auf Machine Learning basierenden Produkt-Empfehlungs- und Klassifikationssystems zur Verbesserung der Produktkategorisierung und Empfehlungsgüte.
\end{itemize}
\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Wissenschaftlicher Assistent RPTU}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{08/2019 - 10/2020}\
\begin{itemize}
    \item Entwicklung einer virtuellen 3D-Umgebung für die Produktionsautomatisierung unter Verwendung von Unreal Engine 4 und Blender.
    \item Datensatz für Deep Learning-Anwendungen erstellen.
    \item Test und Validierung des Datensatzes.
\end{itemize}
\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Projektarbeit}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{11/2018 - 08/2019}\
\begin{itemize}
    \item Thema: Scene Matching
    \item Entwicklung einer virtuellen 3D-Umgebung in Unreal Engine 4 und Tests unter Verwendung von realen Bildern.
    \item Verwendete Tools und Frameworks: : Finroc ( Robotic Framwork verwendetes in RR Lab TU KL), Unreal Engine 4, Blender
\end{itemize}

\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Electromobility Projekt}}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{04/2017 - 06/2017}\
\begin{itemize}
    \item Simulationen von Energieberechnung und Energiemanagement für Hybridfahrzeuge mit MATLABSimulink.
\end{itemize}

\is
{\fontsize{14pt}{14pt}\selectfont
\textcolor{cvblue!90}{\textbf {Junior Engineer}}} \\
\hspace*{1em}\textit{Nirmiti Design Engineers PVT. LTD}\hfill\dates{07/2015 - 06/2016}\
\begin{itemize}
    \item Überprüfung der Fertigungsarbeiten anhand von CAD-Konstruktionen als Nachwuchsingenieur.
    \item Durchführung von Bestandsabgleichen zur Sicherstellung einer korrekten Bestandsführung.
    \item Steuerung des Materialflusses in der Fertigung zur Gewährleistung eines reibungslosen Produktionsablaufs.
\end{itemize}

\headright{Ausbildung}
{\fontsize{12pt}{12pt}\selectfont
\textcolor{cvblue!90}{\textbf {M.Sc. in Nutzfahrzeugtechnik }}} \\
\hspace*{1em}\textit{RPTU Kaiserslautern-Landau}\hfill\dates{10/2016 - 04/2023}\\
\smaller{Thesis title: \textit{Optimierung von Objekterkennungsmodellen und Einsatz von Edge-Geräten }} \\
\smaller{Schwerpunkt : Software Entwicklung, Robotics, Machine Learning, Electomobiliy, Simulation, Comunication Protocols } \\

\is
{\fontsize{12pt}{12pt}\selectfont
\textcolor{cvblue!90}{\textbf {Bachelor of Enginnering in Maschinenbau }}} \\
\hspace*{1em}\textit{Pune Universität (Indien)}\hfill\dates{06/2011 - 06/2015}\\
\smaller{Schwerpunkt : Simulation, MAathamatik, Mechanik, Thermodynamik, CAD/CAM, Fertigungstechnologien } \\




\end{minipage}

\end{document}

"""