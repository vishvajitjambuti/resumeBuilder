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
\usepackage{hyperref}
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

\entrytitle{Development Engineer}{01/2024 - Present}
\entrycompany{Bertrandt AG (Ingolstadt)}
{\color{bodytext}
__JOB_1_DETAILS__
}

\entrytitle{Master's Thesis}{08/2022 - 05/2023}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Developed a real-time object detection system for construction site safety using YOLOv5 and PyTorch to detect personnel and construction equipment.
\item Trained and optimized deep learning models on a GPU cluster, improving detection accuracy and inference performance.
\item Deployed the object detection pipeline on an NVIDIA Jetson Nano and accelerated inference using TensorRT for edge AI applications.
\item Designed and implemented ROS2-based image processing and sensor data pipelines for real-time perception and data integration.
\item Containerized the complete application with Docker, enabling reproducible deployment, simplified maintenance, and portable edge-device execution.
\end{itemize}}

\entrytitle{Software Developer}{04/2021 - 08/2022}
\entrycompany{Elvinci.de GmbH}
{\color{bodytext}
__JOB_2_DETAILS__
}

\newpage
\entrytitle{Intern}{11/2021 - 04/2022}
\entrycompany{Elvinci.de GmbH}
{\color{bodytext}
\begin{itemize}
\item Automated daily operational tasks to improve efficiency and streamline business processes.
\item Performed statistical and predictive analysis of B2B sales data sourced from an ERP system.
\item Designed and executed API test cases throughout the development lifecycle to identify issues early and improve overall API quality.
\item Developed a mobile Android application for warehouse product data collection using Flutter and Dart.
\item Created and executed test cases for the Android application to ensure functionality and reliability.
\item Worked on a product Recommendation and Classification system.
\end{itemize}}

\entrytitle{Research Assistant RPTU}{08/2019 - 10/2020}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Developed a virtual 3D environment for production automation using Unreal Engine 4 and Blender.
\item Created datasets for deep learning applications.
\item Performed testing and validation of the generated datasets.
\end{itemize}}

\entrytitle{Project Work}{11/2018 - 08/2019}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Topic: Scene Matching
\item Developed a virtual 3D environment in Unreal Engine 4 and conducted tests using real images.
\item Tools and Frameworks Used: Finroc (Robotic Framework used in RR Lab TU KL), Unreal Engine 4, Blender
\end{itemize}}

\entrytitle{Electromobility Project}{04/2017 - 06/2017}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Performed energy consumption and energy management simulations for hybrid vehicles using MATLAB/Simulink.
\end{itemize}}

\entrytitle{Junior Engineer}{07/2015 - 06/2016}
\entrycompany{Nirmiti Design Engineers PVT. LTD}
{\color{bodytext}
\begin{itemize}
\item Verified manufacturing work against CAD designs as a Junior Engineer.
\item Conducted inventory reconciliation to ensure accurate inventory records.
\item Coordinated material flow within the production process to ensure smooth manufacturing operations.
\end{itemize}}

% ---- Education ----
\mainhead{EDUCATION}

\entrytitle{M.Sc. in Commercial Vehicle Technology}{10/2016 - 04/2023}
\entrycompany{RPTU Kaiserslautern-Landau}
{\color{bodytext}
\begin{itemize}
\item Thesis title: Optimization of Object Detection Models and Deployment on Edge Devices
\item Focus Areas: Software Development, Robotics, Machine Learning, Electromobility, Simulation, Communication Protocols
\end{itemize}}

\entrytitle{Bachelor of Engineering in  Mechanical Engineering}{06/2011 - 06/2015}
\entrycompany{Pune University (India)}
{\color{bodytext}
\begin{itemize}
\item Focus Areas: Simulation, Mathematics, Mechanics, Thermodynamics, CAD/CAM, Manufacturing Technologies
\end{itemize}}

\end{rightcolumn}
\end{paracol}

\end{document}
"""