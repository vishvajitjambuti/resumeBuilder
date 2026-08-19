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
\section*{Professional Experience}

\timelineentry{01/2024 - Present}{Development Engineer}{Bertrandt AG  (Ingolstadt)}{
  \entrybullets{
  __JOB_1_DETAILS__
  }
}

\timelineentry{08/2022 - 05/2023}{Master Thesis}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
          \item Developed a real-time object detection system for construction site safety using YOLOv5 and PyTorch to detect personnel and construction equipment.
        \item Trained and optimized deep learning models on a GPU cluster, improving detection accuracy and inference performance.
        \item Deployed the object detection pipeline on an NVIDIA Jetson Nano and accelerated inference using TensorRT for edge AI applications.
        \item Designed and implemented ROS2-based image processing and sensor data pipelines for real-time perception and data integration.
        \item Containerized the complete application with Docker, enabling reproducible deployment, simplified maintenance, and portable edge-device execution.
  }
}

\timelineentry{04/2021 - 08/2022}{Software Developer}{Elvinci.de GmbH}{
  \entrybullets{
    __JOB_2_DETAILS__
  }
}

\timelineentry{11/2020 - 04/2021}{Internship}{Elvinci.de GmbH}{
  \entrybullets{
   \item Automated daily operational tasks to improve efficiency and streamline business processes.
    \item Performed statistical and predictive analysis of B2B sales data sourced from an ERP system.
    \item Designed and executed API test cases throughout the development lifecycle to identify issues      early and improve overall API quality.
    \item Developed a mobile Android application for warehouse product data collection using Flutter and    Dart.
    \item Created and executed test cases for the Android application to ensure functionality and           reliability.
    \item Worked on a product Recommendation and Classification system.
  }
}

\timelineentry{08/2019 - 10/2020}{Research Assistant RPTU}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
   \item Developed a virtual 3D environment for production automation using Unreal Engine 4 and Blender.
    \item Created datasets for deep learning applications.
    \item Performed testing and validation of the generated datasets.
  }
}

\timelineentry{11/2018 - 08/2019}{Project Work}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
    \item Topic: Scene Matching
        \item Developed a virtual 3D environment in Unreal Engine 4 and conducted tests using real images.
        \item Tools and Frameworks Used: Finroc (Robotic Framework used in RR Lab TU KL), Unreal Engine 4, Blender
  }
}

\timelineentry{04/2017 - 06/2017}{Electromobility Project}{RPTU Kaiserslautern-Landau}{
  \entrybullets{
   \item Performed energy consumption and energy management simulations for hybrid vehicles using   MATLAB/Simulink.
  }
}

\timelineentry{07/2015 - 06/2016}{Junior Engineer}{NIRMITI DESIGN ENGINEERS PVT. LTD Bezeichnung}{
  \entrybullets{
    \item Verified manufacturing work against CAD designs as a Junior Engineer.
    \item Conducted inventory reconciliation to ensure accurate inventory records.
    \item Coordinated material flow within the production process to ensure smooth manufacturing operations.
  }
}

% ================= EDUCATION =================
\section*{Educational Background}

\timelineentry{10/2016 - 04/2023}{M.Sc. in Commercial Vehicle Technology }{RPTU Kaiserslautern-Landau}{
\begin{itemize}
\item Thesis title: Optimization of Object Detection Models and Deployment on Edge Devices
\item Focus Areas: Software Development, Robotics, Machine Learning, Electromobility, Simulation, Communication Protocols
\end{itemize}
}

\timelineentry{06/2011 - 06/2015}{Bachelor of Engineering in  Mechanical Engineering}{Pune University (India)}{
\begin{itemize}
\item Focus Areas: Simulation, Mathematics, Mechanics, Thermodynamics, CAD/CAM, Manufacturing Technologies
\end{itemize}
}

% ================= SKILLS =================
\section*{Languages \& Skills}
\textbf{Languages:} English (C1) \quad | \quad German (B2)
\begin{itemize}[leftmargin=10pt]
\item Python, C++, C\#, TypeScript, Matlab, SQL, Bash
\item Git, Jira, Docker
\item ROS2, Pytorch, TensorFlow, .NET, React
\item Vector, CANoe, CAPL
\end{itemize}


\end{document}
"""