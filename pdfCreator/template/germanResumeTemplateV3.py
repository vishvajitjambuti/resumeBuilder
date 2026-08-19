template = r"""
\documentclass[9.5pt,a4paper]{article}

\usepackage[top=0.7cm,bottom=0.8cm,left=1cm,right=1cm]{geometry}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{tabularx}
\usepackage{array}
\usepackage[hidelinks]{hyperref}
%\usepackage{helvet}
\usepackage{helvet }
\renewcommand{\familydefault}{\sfdefault}
\usepackage{parskip}
\usepackage{calc}
\pagestyle{empty}
\usepackage{hyperref}
\usepackage{fontawesome5}

% ---------- Colors ----------
\definecolor{brown}{HTML}{1F4E79}
\definecolor{darkbrown}{HTML}{2E5F8A}
\definecolor{textcol}{HTML}{222222}
\definecolor{grey}{HTML}{595959}
\definecolor{lightline}{HTML}{D9D9D9}

% ---------- Section heading style ----------
\titleformat{\section}
  {\Large\bfseries\color{textcol}}
  {}{0em}{}
  [\vspace{-2pt}{\color{lightline}\titlerule[0.8pt]}]
\titlespacing*{\section}{0pt}{8pt}{5pt}

% ---------- Timeline entry macro ----------
% #1 date range   #2 title   #3 organization (optional, can be empty)   #4 bullet items (itemize block)
\newlength{\dtcol}
\setlength{\dtcol}{1.3cm}

\newcommand{\timelineentry}[4]{%
  \noindent
  \begin{tabularx}{\linewidth}{@{}p{\dtcol}!{\color{brown}\vrule width 1.2pt}X@{}}
    \raggedright\footnotesize\color{grey} #1 &
    \hspace{0.35cm}\begin{minipage}[t]{\dimexpr\linewidth-0.35cm\relax}
      \textbf{\normalsize\color{textcol} #2}{\footnotesize\color{brown}\ --\ #3}\\[0pt]
      #4
    \end{minipage}
  \end{tabularx}
  \vspace{1pt}
}

\newcommand{\entrybullets}[1]{%
  \begin{itemize}[leftmargin=12pt,itemsep=0pt,topsep=1pt,parsep=0pt,label={\small\textbullet}]
  #1
  \end{itemize}
}

% ---------- Skill tag macro ----------
\newcommand{\skilltag}[1]{%
  \colorbox{darkbrown}{\parbox[c][0.62cm][c]{2.95cm}{\centering\footnotesize\bfseries\color{white} #1}}%
}

\begin{document}

% ================= HEADER =================
\noindent
\begin{minipage}[t]{3cm}
\vspace{0pt}
\includegraphics[width=2.7cm,height=3.7cm,keepaspectratio]{__IMAGE_PATH__}
\end{minipage}%
\begin{minipage}[t]{\dimexpr\linewidth-3cm\relax}
\vspace{0pt}
{\huge\bfseries\color{brown} Vishvajit Jambuti}\\[7pt]
\begin{minipage}[t]{0.5\linewidth}

{\footnotesize\color{grey} \textbullet\ \ Ettinger str 1,  85057 Ingolstadt}\\[5pt]
{\footnotesize\color{grey} \textbullet\ \ Germany}\\[5pt]
%{\footnotesize\color{grey} \textbullet\ \ 15/10/1993}
{\footnotesize\color{brown} \textbullet\ \ \href{https://www.linkedin.com/in/vishvajit-jambuti-511b7a17b/}{\faLinkedin\ \ Vishvajit Jambuti}}
\end{minipage}%
\begin{minipage}[t]{0.5\linewidth} 
{\footnotesize\color{grey} \textbullet\ \ +49 17666070455}\\[5pt]
{\footnotesize\color{grey} \textbullet\ \ vishvajitjambuti003@gmail.com} \\[5pt]
{\footnotesize\color{grey} \textbullet\ \ \href{https://github.com/vishvajitjambuti}{\faGithub\ \ vishvajit-jambuti}}
\end{minipage}
\end{minipage}

\vspace{9.50pt}

{\small\color[HTML]{333333}
__PROFILE_DETAILS__
}


% ================= PROFESSIONAL EXPERIENCE =================
\section*{Berufserfahrung}

\timelineentry{01/2024 - Present}{Development Engineer}{Bertrandt AG  (Ingolstadt)}{
  \entrybullets{
    __JOB_1_DETAILS__
  }
}

\timelineentry{08/2022 - 05/2023}{Masterarbeit}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
        \item Entwicklung eines Echtzeit-Objekterkennungssystems für die Sicherheit auf Baustellen mittels YOLOv5 und PyTorch zur Erkennung von Personal und Baumaschinen.
        \item Training und Optimierung von Deep-Learning-Modellen auf einem GPU-Cluster zur Verbesserung von Erkennungsgenauigkeit und Inferenzleistung.
        \item Bereitstellung der Objekterkennungs-Pipeline auf einem NVIDIA Jetson Nano sowie Beschleunigung der Inferenz mittels TensorRT für Edge-AI-Anwendungen.
        \item Konzeption und Implementierung von ROS2-basierten Bildverarbeitungs- und Sensordaten-Pipelines für Echtzeit-Wahrnehmung und Datenintegration.
        \item Containerisierung der gesamten Anwendung mit Docker zur Ermöglichung reproduzierbarer Deployments, vereinfachter Wartung und portabler Ausführung auf Edge-Geräten.
  }
}

\timelineentry{04/2021 - 08/2022}{Softwareentwickler}{Elvinci.de GmbH}{
  \entrybullets{
   __JOB_2_DETAILS__
  }
}

\timelineentry{11/2020 - 04/2021}{Praktikum}{Elvinci.de GmbH}{
  \entrybullets{
    \item Automatisierung täglicher betrieblicher Aufgaben zur Effizienzsteigerung und Optimierung von Geschäftsprozessen.
    \item Durchführung statistischer und prädiktiver Analysen von B2B-Verkaufsdaten aus einem ERP-System.
    \item Konzeption und Durchführung von API-Testfällen über den gesamten Entwicklungszyklus hinweg zur frühzeitigen Fehlererkennung und Verbesserung der allgemeinen API-Qualität.
    \item Entwicklung einer mobilen Android-Anwendung zur Erfassung von Lagerproduktdaten mit Flutter und Dart.
    \item Erstellung und Durchführung von Testfällen für die Android-Anwendung zur Sicherstellung von Funktionalität und Zuverlässigkeit.
    \item Mitarbeit an einem Produkt-Empfehlungs- und Klassifizierungssystem.
  }
}

\timelineentry{08/2019 - 10/2020}{Wissenschaftlicher Assistent RPTU}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
    \item Entwicklung einer virtuellen 3D-Umgebung für Produktionsautomatisierung mit Unreal Engine 4 und Blender.
    \item Erstellung von Datensätzen für Deep-Learning-Anwendungen.
    \item Durchführung von Tests und Validierung der generierten Datensätze.
  }
}

\timelineentry{11/2018 - 08/2019}{Projektarbeit}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
    \item Thema: Scene Matching
    \item Entwicklung einer virtuellen 3D-Umgebung in Unreal Engine 4 und Durchführung von Tests mit realen Bildern.
    \item Verwendete Tools und Frameworks: Finroc (Robotik-Framework der RR Lab TU KL), Unreal Engine 4, Blender
  }
}

\timelineentry{04/2017 - 06/2017}{Electromobility Projekt}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
   \item Durchführung von Simulationen zum Energieverbrauch und Energiemanagement für Hybridfahrzeuge mit MATLAB/Simulink.
  }
}

\timelineentry{07/2015 - 06/2016}{Junior Engineer}{NIRMITI DESIGN ENGINEERS PVT. LTD Bezeichnung}{
  \entrybullets{
    \item Überprüfung der Fertigungsarbeiten anhand von CAD-Konstruktionen als Junior Engineer.
    \item Durchführung von Bestandsabgleichen zur Sicherstellung korrekter Lagerbestände.
    \item Koordination des Materialflusses innerhalb des Produktionsprozesses zur Gewährleistung reibungsloser Fertigungsabläufe.
  }
}

% ================= EDUCATION =================
\section*{Educational Background}

\timelineentry{10/2016 - 04/2023}{M.Sc. in Commercial Vehicle Technology }{RPTU Kaiserslautern-Landau}{
\begin{itemize}
\item Titel der Abschlussarbeit: Optimierung von Objekterkennungsmodellen und Deployment auf Edge-Geräten
\item Schwerpunkte: Softwareentwicklung, Robotik, Machine Learning, Elektromobilität, Simulation, Kommunikationsprotokolle
\end{itemize}
}

\timelineentry{06/2011 - 06/2015}{Bachelor of Engineering in  Mechanical Engineering}{Pune University (India)}{
\begin{itemize}
\item Schwerpunkt : Simulation, MAathamatik, Mechanik, Thermodynamik, CAD/CAM, Fertigungstechnologien
\end{itemize}
}

% ================= SKILLS =================
\section*{Sprachen \& Fähigkeiten}


     \textbf{Sprachen:} Englisch (C1) \quad | \quad Deutsch (B2)

    \begin{itemize} %[leftmargin=10pt]
    \item Python, C++, C\#, TypeScript, Matlab, SQL, Bash
    \item Git, Jira, Docker
    \item ROS2, Pytorch, TensorFlow, .NET, React
    \item Vector, CANoe, CAPL
    \end{itemize}



\end{document}
"""