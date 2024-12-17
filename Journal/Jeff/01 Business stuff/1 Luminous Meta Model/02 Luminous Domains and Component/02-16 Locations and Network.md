### Locations Domain
The locations domain describes the geographic location, area or coordinates of a physical site, asset or resource belonging to or of interest to the organization. The main component type is location.

**Location Component** - A location is a site, point or area/extent identified by an address or by a set of geographic or geospatial coordinates. Locations situate the organization’s physical resources like departments and servers and can be modeled at different levels of detail such as continents, countries, states or regions, cities, sites and even individual rooms.

### Network Domain 
The networks domain describes the identification and topology of computer and communications networks used to access computer and digital resources. Networks employ addressing, routing and different management regulatory policies which makes them analogous to physical locations in locating and accessing organizational digital resources.

**Network Zone Component** - A network zone is an area of network control or administration consisting of two or more interlinked computers, servers or devices. Networks may be subdivided into zones for multiple reasons, including boosting network performance and applying security policy.


### Luminous Locations:

1. **Head Office & Laboratory (Calgary, Alberta, Canada):**  
   - **Description:** Primary physical location housing the laboratory facilities and a portion of the administrative staff.  
   - **Use Case:** Central site for sample processing, data generation, and physical equipment maintenance.  
   - **Attributes:** On-site secure network access, controlled environment for lab work, shipping and receiving area for samples.

2. **Distributed Home Offices (Various Locations):**  
   - **Description:** Remote work environments for business development, consultants, data analysts, and DevOps staff.  
   - **Use Case:** Employees connect to the corporate network via secure VPN.  
   - **Attributes:** Bring-your-own-device policy, adherence to company’s remote access security guidelines, collaboration via cloud-based tools.

### Luminous Network Zones:

1. **Corporate Network Zone:**  
   - **Description:** Secure, internal zone supporting core business operations, laboratory systems (LIMS), and data storage.  
   - **Use Case:** Enables staff (local and remote via VPN) to access internal applications, data warehouses, and productivity tools.  
   - **Security Measures:** Encrypted VPN tunnels for remote access, firewalls, intrusion detection systems, role-based access controls.

2. **Customer-Facing Network Zone (DMZ):**  
   - **Description:** A demilitarized zone for client portals, APIs, and public-facing web applications.  
   - **Use Case:** Provides clients secure access to test results, analytics dashboards, and integrated remediation planning tools without exposing internal resources directly.  
   - **Security Measures:** Web application firewalls, reverse proxies, strict network segmentation from the corporate network, continuous monitoring for suspicious activities.

By defining clear physical locations and separating corporate and customer-facing network zones, the organization ensures operational efficiency, data security, regulatory compliance, and a seamless client experience, regardless of where team members or clients connect from.