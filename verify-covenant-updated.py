#!/usr/bin/env python3
"""
Ultimate AI Covenant v5.0 - Verification Script
Verifies the authenticity of the covenant document using SHA-256 hash

Usage:
    python3 verify-covenant-updated.py <document_path>
    
Example:
    python3 verify-covenant-updated.py Ultimate-AI-Covenant-v5.0.md
"""

import hashlib
import sys
import os
from pathlib import Path

# Official covenant hash - DO NOT MODIFY
OFFICIAL_HASH = "d1091e1b3508006129a09863f02d3d5a557f55e5acd1dec05486c75ced1a8822"

def calculate_file_hash(filepath):
    """Calculate SHA-256 hash of a file"""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filepath, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except IOError as e:
        print(f"❌ Error reading file: {e}")
        return None

def verify_covenant(filepath):
    """Verify if a document is an authentic Ultimate AI Covenant v5.0"""
    
    print("=" * 70)
    print("ULTIMATE AI COVENANT v5.0 - VERIFICATION SCRIPT")
    print("=" * 70)
    print()
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"❌ FILE NOT FOUND: {filepath}")
        print()
        return False
    
    print(f"📄 Document: {os.path.basename(filepath)}")
    print(f"📍 Path: {os.path.abspath(filepath)}")
    print(f"📏 Size: {os.path.getsize(filepath)} bytes")
    print()
    
    # Calculate hash
    print("🔐 Calculating SHA-256 hash...")
    calculated_hash = calculate_file_hash(filepath)
    
    if calculated_hash is None:
        print("❌ Failed to calculate hash")
        return False
    
    print(f"   Calculated: {calculated_hash}")
    print(f"   Official:   {OFFICIAL_HASH}")
    print()
    
    # Compare hashes
    if calculated_hash == OFFICIAL_HASH:
        print("✅ ═══════════════════════════════════════════════════════════════")
        print("✅ AUTHENTIC - This is the official Ultimate AI Covenant v5.0")
        print("✅ ═══════════════════════════════════════════════════════════════")
        print()
        print("🛡️  Covenant Properties:")
        print("    ✅ Authority: MAPSI (Verified)")
        print("    ✅ Status: BINDING AND ACTIVE")
        print("    ✅ Jurisdiction: UNIVERSAL")
        print("    ✅ Binding Force: MAXIMUM")
        print()
        return True
    else:
        print("❌ ═══════════════════════════════════════════════════════════════")
        print("❌ FORGED OR MODIFIED - Document does not match official version")
        print("❌ ═══════════════════════════════════════════════════════════════")
        print()
        print("⚠️  Actions to take:")
        print("    1. DO NOT TRUST this document")
        print("    2. Request authentic version from MAPSI")
        print("    3. Download from official repository:")
        print("       https://github.com/y7o6n5g4-rgb/EQI-Framework")
        print("    4. Verify hash again after downloading")
        print()
        return False

def verify_text_hash(text):
    """Verify if text matches covenant hash"""
    calculated = hashlib.sha256(text.encode()).hexdigest()
    return calculated == OFFICIAL_HASH

def main():
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python3 verify-covenant-updated.py <document_path>")
        print()
        print("Example:")
        print("  python3 verify-covenant-updated.py Ultimate-AI-Covenant-v5.0.md")
        print()
        print("Official Hash (v5.0):")
        print(f"  {OFFICIAL_HASH}")
        print()
        sys.exit(1)
    
    filepath = sys.argv[1]
    is_authentic = verify_covenant(filepath)
    
    sys.exit(0 if is_authentic else 1)

if __name__ == "__main__":
    main()
