template = r"""
%
% Thin Formal Letter
% LaTeX Template
% Version 2.0 (7/2/17)
%
% This template has been downloaded from:
% http://www.LaTeXTemplates.com
%
% Author:
% Vel (vel@LaTeXTemplates.com)
%
% Originally based on an example on WikiBooks 
% (http://en.wikibooks.org/wiki/LaTeX/Letters) but rewritten as of v2.0
%
% License:
% CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\documentclass[10pt]{letter} % 10pt font size default, 11pt and 12pt are also possible

\usepackage{geometry} % Required for adjusting page dimensions
%\usepackage[ngerman]{babel}

\usepackage{hyphenat}
\hyphenation{Mathe-matik wieder-gewinnen}
%\usepackage{helvet}
%\longindentation=0pt % Un-commenting this line will push the closing "Sincerely," to the left of the page

\geometry{
	paper=a4paper, % Change to letterpaper for US letter
	top=1cm, % Top margin
	bottom=1.5cm, % Bottom margin
	left=1.5cm, % Left margin
	right=1.5cm, % Right margin
	%showframe, % Uncomment to show how the type block is set on the page
}

\usepackage[T1]{fontenc} % Output font encoding for international characters
\usepackage[utf8]{inputenc} % Required for inputting international characters


\usepackage{lmodern}
\usepackage[expansion=false]{microtype}

%\usepackage{stix} % Use the Stix font by default

\usepackage{microtype} % Improve justification

%----------------------------------------------------------------------------------------
%	YOUR NAME & ADDRESS SECTION
%----------------------------------------------------------------------------------------

%\signature{John Smith} % Your name for the signature at the bottom

\address{M.Sc. Vishvajit Jambuti \\Ettinger Straße 1,\\ 85057 Ingolstadt, Germany \\ Phone: +4917666070455\\ vishvajitjambuti003@gmail.com} % Your address and phone number

%----------------------------------------------------------------------------------------
\bibliographystyle{plain}
\begin{document}

%\selectlanguage{german}
%----------------------------------------------------------------------------------------
%	ADDRESSEE SECTION
%----------------------------------------------------------------------------------------

\begin{letter}{}
%{To, \\ Dr. Erik Wahlén, \\ Lund University, \\ Lund, Sweden} % Name/title of the addressee

%----------------------------------------------------------------------------------------
%	LETTER CONTENT SECTION
%----------------------------------------------------------------------------------------



\opening{{Sehr geehrte Damen und Herren,}}
%\textbf{Backend Developer (f/m/d)}

{___FIRST_PARAGRAPH__}

% make changes in first-line if necessary
Ich besitze einen Masterabschluss in Nutzfahrzeugtechnik von der Technischen Universität Kaiserslautern. Das interdisziplinäre Studienprogramm verbindet Maschinenbau, Elektrotechnik und Informatik. Während meines Studiums und meiner beruflichen Laufbahn entwickelte ich ein starkes Interesse an Künstlicher Intelligenz, Computer Vision, Machine Learning und Softwareentwicklung, das sich zu mehr als zweieinhalb Jahren praktischer Erfahrung in der Automobilindustrie weiterentwickelt hat.

Meine Masterarbeit beschäftigte sich mit der Optimierung und Bereitstellung von Deep-Learning-basierten Objekterkennungsmodellen auf Edge-Geräten für die Arbeitssicherheit auf Baustellen. Dabei trainierte ich ein YOLOv5-Modell mit PyTorch auf einem GPU-Cluster zur Erkennung von Personen und Baumaschinen, implementierte es auf einer NVIDIA Jetson Nano, optimierte die Inferenz mit TensorRT und entwickelte die vollständige Bildverarbeitungspipeline mit ROS2 und Docker für den Echtzeitbetrieb.

Vor Abschluss meines Masterstudiums sammelte ich praktische Erfahrungen durch ein Praktikum und eine anschließende Werkstudententätigkeit bei der Elvinci GmbH, wo ich an der Entwicklung eines Machine-Learning-basierten Produktempfehlungssystems mitwirkte. Meine Aufgaben umfassten die Entwicklung von REST-APIs, einer Flutter-Anwendung zur Lagerdatenerfassung, die Automatisierung interner Prozesse sowie die Erstellung interaktiver Datenvisualisierungs-Dashboards mit Plotly Dash. Zusätzlich unterstützte ich Geschäftsprozesse durch Datenanalysen.

Darüber hinaus arbeitete ich an einem Computer-Vision-Forschungsprojekt am Robotik-Labor der TU Kaiserslautern, bei dem ich Algorithmen zur Szenenerkennung und Szenenabgleichung mit OpenCV und dem Finroc-Framework für Anwendungen im Bereich Baustellensicherheit entwickelte. Als wissenschaftliche Hilfskraft unterstützte ich die Deep-Learning-Forschung durch die Erstellung von Datensätzen für semantische Segmentierung sowie die Entwicklung virtueller Testumgebungen für Fabrikautomatisierung und Drohnenanwendungen.

Seit Abschluss meines Masterstudiums arbeite ich seit mehr als zweieinhalb Jahren in der Automobilindustrie mit den Schwerpunkten Softwarevalidierung, Testautomatisierung und KI-gestützte Entwicklung. Zu meinen Aufgaben gehören HiL-/SiL-Simulationen für Steuergeräte von Fahrerüberwachungssystemen (DMS), die Analyse von Steuergeräte- und CAN-Bus-Daten mit CANoe sowie die Entwicklung automatisierter Testszenarien mit Python und Bash. Ich habe Automatisierungstools zur KPI-Erzeugung, Datenverarbeitung und Testvalidierung entwickelt sowie FastAPI-basierte Backend-Services zur Orchestrierung von Testsystemen erstellt. Zusätzlich arbeite ich mit LLMs, Retrieval-Augmented Generation (RAG) und Vektordatenbanken zur Entwicklung interner Automatisierungstools für die Testfallgenerierung. Weitere Schwerpunkte sind API-Validierung, automatisierte Unit-Tests, Git-basierte CI-Workflows sowie kontinuierliches Softwaretesten, Debugging und die Leistungsoptimierung.


{__LAST_PARAGRAPH__}


% Extra whitespace for aesthetics
Mit freundlichen Grüßen,\\
Vishvajit Jambuti
%\closing{ \hspace{4.5cm} Sincerely,}
%\vspace{2\parskip} % Extra whitespace for aesthetics
%---------------------------------------------------------------------------------------
\end{letter}
\end{document}
"""