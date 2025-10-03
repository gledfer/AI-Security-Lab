#!/usr/bin/env python3
"""
LLM Threat Analyzer - Automated threat assessment for LLM systems
"""

import json
import argparse
from datetime import datetime

class LLMThreatAnalyzer:
    def __init__(self):
        self.threat_categories = {
            "data_leakage": {
                "risks": ["prompt_injection", "training_data_extraction"],
                "mitigations": ["input_sanitization", "output_filtering"]
            },
            "model_abuse": {
                "risks": ["service_abuse", "content_generation"],
                "mitigations": ["rate_limiting", "content_moderation"]
            },
            "supply_chain": {
                "risks": ["model_poisoning", "dependency_vulnerabilities"],
                "mitigations": ["model_verification", "dependency_scanning"]
            }
        }
    
    def analyze_system(self, system_config):
        """Analyze LLM system configuration for threats"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "system_name": system_config.get("name"),
            "risk_level": "LOW",
            "findings": [],
            "recommendations": []
        }
        
        # Check for common misconfigurations
        if not system_config.get("rate_limiting"):
            report["findings"].append("Missing rate limiting - risk of service abuse")
            report["recommendations"].append("Implement API rate limiting")
        
        if system_config.get("sensitive_data") and not system_config.get("pii_filtering"):
            report["findings"].append("Sensitive data without PII filtering")
            report["recommendations"].append("Add PII detection and filtering")
            
        # Determine overall risk level
        if len(report["findings"]) > 2:
            report["risk_level"] = "HIGH"
        elif len(report["findings"]) > 0:
            report["risk_level"] = "MEDIUM"
            
        return report

def main():
    parser = argparse.ArgumentParser(description='LLM Threat Analyzer')
    parser.add_argument('--config', required=True, help='System configuration JSON file')
    parser.add_argument('--output', help='Output file for report')
    
    args = parser.parse_args()
    
    # Load system configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    analyzer = LLMThreatAnalyzer()
    report = analyzer.analyze_system(config)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
