# Simulating an ATS scoring system for the given CV
import re

# Keywords and weightage typically valued by ATS in embedded engineering roles
keywords = {
    "Embedded C": 10, "RTOS": 8, "Embedded Linux": 10, "Bootloader": 7, "Device Tree": 7,
    "Kernel Modules": 7, "ARM Cortex-M": 10, "Microcontrollers": 8, "MPUs": 6,
    "Protocols": 6, "UART": 6, "SPI": 6, "I2C": 6, "Ethernet": 6,
    "Debugging": 7, "Oscilloscope": 7, "Logic Analyzers": 7, "Git": 7,
    "Jira": 5, "Confluence": 5, "GCC": 7, "VS Code": 5,
    "ISO 26262": 8, "Functional Safety": 8, "Compiler": 7, "Firmware": 10,
    "Board bring-up": 9, "System Validation": 8, "Automotive": 7,
    "Defense": 6, "Avionics": 6, "Machine Learning": -5,  # Penalizing irrelevant terms
}

# Extract text from CV
cv_text = """
Embedded Engineer with 6+ years of experience in microcontroller-based firmware development, real-time systems, and board bring-ups for avionics, defense, and industrial applications. Proficient in Embedded C, ARM Cortex, RTOS, and Embedded Linux. Strong debugging and hardware testing skills. Currently exploring Embedded Linux & MPU development for upskilling in next-generation embedded systems.

Key Skills:
- Embedded Software Development: C, Embedded C
- Microcontrollers & MPUs: ARM Cortex-M, PIC, Atmel AVR
- Embedded Linux: Bootloader, Device Tree, Kernel Modules
- Protocols & Peripherals: UART, SPI, I2C, Ethernet
- Debugging & Testing: Oscilloscope, Logic Analyzers
- Version Control: Git
- Tools & IDEs: GCC, VS Code
- Project Documentation & Collaboration: Jira, Confluence, GitHub

Work Experience:
Embedded Systems Engineer | Data Patterns | 3 Years, 9 Months
- Designed and developed firmware for defense & avionics applications.
- Key Projects: LCD Backlight System for LCA Tejas, UHF Communication for Sonobuoy, VHF/UHF Telecommand Telemetry for ISRO INS2-TD Ground Station / OnBoard Computer, Reaction Wheel, GPS module.
- Led board bring-ups and microcontroller firmware development.
- Collaborated with RF & Hardware teams for system integration.

Function Developer | Bosch (BMW Customer Engineering Team) | 1 Year, 8 Months
- Developed and optimized control logic for Thermal Devices Package (BMW S68T0 engine), improving cold start efficiency by integrating PI loops and refined entry/exit logics. Leveraged ASCET tool for function development, with critical components implemented manually for enhanced performance.
- Ensured Functional Safety compliance with ISO 26262 by verifying Unit Tests (UT) and System Functionality Tests (SFT) at BC level / PVER level using TPT tool, focusing on validating system stability and error handling to mitigate potential safety risks.

Volvo Team – Embedded Systems Engineer
- Brought up an evaluation board for a 2K camera module with a 3.2 Gbps payload over MIPI CSI.
- Configured camera registers, serializer, and deserializer for data transfer.
- Enabled high-bandwidth image streaming via DMA engine over MIPI CSI.
- Successfully completed core integration, delivering proof-of-concept validation before the project was discontinued due to business restructuring.

Software Engineer | Microchip Technology | Present
- Verified New Part / New Silicon before public release, ensuring hardware and software validation for embedded systems.
- Developed a framework to test and validate MPLAB VS Code extensions for 8/16/32-bit devices against compatible compilers.

Certifications & Training:
- Advanced C Programming for Embedded Systems (Completed, Vector Institute)

Achievements & Innovations:
- Received accolades from URSC LEO department directors for contributions to ISRO INS2-TD Ground Station & OnBoard Computer firmware development.
- Winner of Department-Level Hackathon at Bosch for developing scripts to analyze ELF and HEX files using map files, improving code size and memory efficiency by optimizing compiler flags in compliance with automotive safety standards.
- Advocated for Rust support in Microchip’s development tools, proposing XC compiler integration to explore compatibility with ARM Cortex-M architectures.
- Proposed a WiFi-based flashing and debugging tool as an alternative to PicKit 5, enabling wireless code flashing and real-time log streaming over WiFi, similar to PuTTY for serial debugging.

Projects & Contributions:
- Due to the nature of past work in defense, automotive, and semiconductor industries, project details are protected under NDA agreements.
- Hands-on experience in Embedded Linux, RTOS, and board bring-ups with real-world applications in avionics, automotive, and industrial domains.
- Strong contributor to internal R&D improvements, providing insights on compiler optimizations, functional safety compliance, and next-gen embedded tool development.
"""

# Scoring ATS match percentage
score = sum(weight for keyword, weight in keywords.items() if re.search(rf"\b{re.escape(keyword)}\b", cv_text, re.IGNORECASE))
max_score = sum(abs(weight) for weight in keywords.values())  # Normalize to 100%

# Convert score to percentage
ats_match_percentage = (score / max_score) * 100
print(ats_match_percentage)