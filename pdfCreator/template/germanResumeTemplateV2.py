template = r"""\documentclass[9pt]{extarticle}

% ---------- Packages ----------
\usepackage[a4paper,left=0.35in,right=0.35in,top=0.35in,bottom=0.35in]{geometry}
\usepackage{paracol}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{eso-pic}
\usepackage{fontspec}
\usepackage{tabto}
\usepackage[skip=0pt]{parskip}
\usepackage{ragged2e}
\usepackage{fontawesome}
\usepackage[hidelinks]{hyperref}
\usepackage{hyperref}

% ---------- Fonts (Calibri, matching original) ----------
\setmainfont{Carlito}[
  BoldFont = Carlito Bold,
  ItalicFont = Carlito Italic,
  BoldItalicFont = Carlito Bold Italic
]

% ---------- Colors (extracted from original document) ----------
\definecolor{navy}{HTML}{1F3864}      % section headings / accent lines
\definecolor{darktext}{HTML}{1A1A1A}  % name (2nd word), job titles
\definecolor{bodytext}{HTML}{333333}  % body / bullet text
\definecolor{sidetext}{HTML}{262626}  % sidebar text
\definecolor{dategray}{HTML}{666666}  % date ranges
\definecolor{companyblue}{HTML}{2E74B5} % italic company / institute names
\definecolor{sidebarbg}{HTML}{F2F2F2} % sidebar background fill

% ---------- Sidebar width (matches 3200/10506 table ratio) ----------
\newlength{\sidebarwidth}
\setlength{\sidebarwidth}{0.35\dimexpr\paperwidth-0.7in\relax}
%\setlength{\sidebarwidth}{0.22\dimexpr\paperwidth-0.7in\relax}
\setcolumnwidth{0.30\dimexpr\paperwidth-0.7in\relax,
                0.70\dimexpr\paperwidth-0.7in\relax}

% ---------- Gray sidebar background repeated on every page ----------
\AddToShipoutPictureBG*{%
  \begin{tikzpicture}[remember picture,overlay]
    \fill[sidebarbg] (current page.north west) rectangle
      ([xshift=\sidebarwidth] current page.south west);
  \end{tikzpicture}%
}

% ---------- Helper commands ----------
\setlist[itemize]{leftmargin=*, itemsep=1pt, topsep=2pt, parsep=0pt, label=\textbullet}

% Sidebar section heading: bold navy caps with a navy rule underneath
\newcommand{\sidehead}[1]{%
  \par\vspace{6pt}%
  {\color{navy}\bfseries\fontsize{9}{11}\selectfont #1}\par
  \vspace{1pt}
  %{\color{navy}\rule{\sidebarwidth  }{0.6pt}}
 {\color{navy}\rule{\linewidth}{0.6pt}}
}

% Main-column section heading: bold navy caps, larger, thicker navy rule
\newcommand{\mainhead}[1]{%
  \par\vspace{7pt}%
  {\color{navy}\bfseries\fontsize{12}{14}\selectfont #1}\par
  \vspace{1pt}
  
  {\color{navy}\rule{\linewidth}{1pt}}\par\vspace{4pt}
}

% Job / education entry title line: bold dark title .... bold gray date, right aligned
\newcommand{\entrytitle}[2]{%
  \par\vspace{5pt}
  {\color{darktext}\bfseries\fontsize{10}{12}\selectfont #1}\hfill
  {\color{dategray}\bfseries\fontsize{9}{11}\selectfont #2}\par
}

% Company / institute name, italic blue
\newcommand{\entrycompany}[1]{%
  \vspace{1pt}
  {\color{companyblue}\itshape\fontsize{9}{11}\selectfont #1}\par
  \vspace{2pt}
}

\pagestyle{empty}
\frenchspacing

\begin{document}

\begin{paracol}{2}
\setcolumnwidth{0.25\dimexpr\paperwidth-0.7in\relax,0.75\dimexpr\paperwidth-0.7in\relax}
\setlength{\columnsep}{0.3in}

% ======================= LEFT SIDEBAR =======================
\begin{leftcolumn}
\color{sidetext}
\RaggedRight
\fontsize{8.5}{10.5}\selectfont

\begin{center}
\includegraphics[width=2in]{__IMAGE_PATH__}
\end{center}
\sidehead{CONTACT DETAILS}\\
vishvajitjambuti003@gmail.com\par
+4917666070455\par
Ettinger Stra\ss e 1,\par
85057 Ingolstadt\par

\sidehead{PERSONAL INFO \& LANGUAGE}\\
%Birth Date: 15/10/1993\par
\textcolor{navy}{\href{https://www.linkedin.com/in/vishvajit-jambuti-511b7a17b/}{\faLinkedin\ \ Vishvajit Jambuti}}\par
English: C1\par
German: B2\par

\sidehead{SKILLS}
\begin{itemize}[leftmargin=10pt]
\item Python, C++, C\#, TypeScript, Matlab, SQL, Bash
\item Git, Jira, Docker
\item FastAPI, .NET, React
\item Vector, CANoe, CAPL
\end{itemize}

{\color{sidebarbg}
\sidehead{}
__KEYWORDS__

}


\end{leftcolumn}

% ======================= RIGHT MAIN COLUMN =======================
\begin{rightcolumn}
\RaggedRight

% ---- Name ----
\vspace{2pt}
{\color{navy}\bfseries\fontsize{20}{22}\selectfont VISHVAJIT }%
{\color{darktext}\bfseries\fontsize{20}{22}\selectfont JAMBUTI}\par

% ---- Profile ----
\mainhead{PROFILE}
{\color{bodytext}\fontsize{9.5}{12}\selectfont
__PROFILE_DETAILS__
}

% ---- Experience ----
\mainhead{EXPERIENCE}

\entrytitle{Entwicklungsingenieur}{01/2024 - Heute}
\entrycompany{Bertrandt AG (Ingolstadt)}
{\color{bodytext}
__JOB_1_DETAILS__
}

\entrytitle{Masterarbeit}{08/2022 - 05/2023}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Entwicklung eines Echtzeit-Objekterkennungssystems für die Sicherheit auf Baustellen mittels YOLOv5 und PyTorch zur Erkennung von Personal und Baumaschinen.
\item Training und Optimierung von Deep-Learning-Modellen auf einem GPU-Cluster zur Verbesserung von Erkennungsgenauigkeit und Inferenzleistung.
\item Bereitstellung der Objekterkennungs-Pipeline auf einem NVIDIA Jetson Nano sowie Beschleunigung der Inferenz mittels TensorRT für Edge-AI-Anwendungen.
\item Konzeption und Implementierung von ROS2-basierten Bildverarbeitungs- und Sensordaten-Pipelines für Echtzeit-Wahrnehmung und Datenintegration.
\item Containerisierung der gesamten Anwendung mit Docker zur Ermöglichung reproduzierbarer Deployments, vereinfachter Wartung und portabler Ausführung auf Edge-Geräten.
\end{itemize}}

\entrytitle{Softwareentwickler}{04/2021 - 08/2022}
\entrycompany{Elvinci.de GmbH}
{\color{bodytext}
__JOB_2_DETAILS__
}
\newpage
\entrytitle{Praktikum}{11/2021 - 04/2022}
\entrycompany{Elvinci.de GmbH}
{\color{bodytext}
\begin{itemize}
\item Automatisierung täglicher betrieblicher Aufgaben zur Effizienzsteigerung und Optimierung von Geschäftsprozessen.
\item Durchführung statistischer und prädiktiver Analysen von B2B-Verkaufsdaten aus einem ERP-System.
\item Konzeption und Durchführung von API-Testfällen über den gesamten Entwicklungszyklus hinweg zur frühzeitigen Fehlererkennung und Verbesserung der allgemeinen API-Qualität.
\item Entwicklung einer mobilen Android-Anwendung zur Erfassung von Lagerproduktdaten mit Flutter und Dart.
\item Erstellung und Durchführung von Testfällen für die Android-Anwendung zur Sicherstellung von Funktionalität und Zuverlässigkeit.
\item Mitarbeit an einem Produkt-Empfehlungs- und Klassifizierungssystem.
\end{itemize}}

\entrytitle{Wissenschaftlicher Assistent RPTU}{08/2019 - 10/2020}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Entwicklung einer virtuellen 3D-Umgebung für Produktionsautomatisierung mit Unreal Engine 4 und Blender.
\item Erstellung von Datensätzen für Deep-Learning-Anwendungen.
\item Durchführung von Tests und Validierung der generierten Datensätze.
\end{itemize}}

\entrytitle{Projektarbeit}{11/2018 - 08/2019}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Thema: Scene Matching
\item Entwicklung einer virtuellen 3D-Umgebung in Unreal Engine 4 und Durchführung von Tests mit realen Bildern.
\item Verwendete Tools und Frameworks: Finroc (Robotik-Framework der RR Lab TU KL), Unreal Engine 4, Blender
\end{itemize}}

\entrytitle{Electromobility Project}{04/2017 - 06/2017}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Durchführung von Simulationen zum Energieverbrauch und Energiemanagement für Hybridfahrzeuge mit MATLAB/Simulink.
\end{itemize}}

\entrytitle{Junior Ingenieur}{07/2015 - 06/2016}
\entrycompany{Nirmiti Design Engineers PVT. LTD}
{\color{bodytext}
\begin{itemize}
\item Überprüfung der Fertigungsarbeiten anhand von CAD-Konstruktionen als Junior Engineer.
\item Durchführung von Bestandsabgleichen zur Sicherstellung korrekter Lagerbestände.
\item Koordination des Materialflusses innerhalb des Produktionsprozesses zur Gewährleistung reibungsloser Fertigungsabläufe.
\end{itemize}}

% ---- Education ----
\mainhead{EDUCATION}

\entrytitle{M.Sc. in Commercial Vehicle Technology}{10/2016 - 04/2023}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Titel der Abschlussarbeit: Optimierung von Objekterkennungsmodellen und Deployment auf Edge-Geräten
\item Schwerpunkte: Softwareentwicklung, Robotik, Machine Learning, Elektromobilität, Simulation, Kommunikationsprotokolle
\end{itemize}}

\entrytitle{Bachelor of Engineering in Maschinenbau}{06/2011 - 06/2015}
\entrycompany{Pune University (India)}
{\color{bodytext}
\begin{itemize}
\item Schwerpunkt : Simulation, MAathamatik, Mechanik, Thermodynamik, CAD/CAM, Fertigungstechnologien
\end{itemize}}

\end{rightcolumn}
\end{paracol}

\end{document}
"""