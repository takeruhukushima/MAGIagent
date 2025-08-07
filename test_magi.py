#!/usr/bin/env python3
"""
Test script to verify MAGI agent can be imported and initialized.
"""

try:
    # Try importing the MAGI agent
    from MAGI import root_agent, create_magi_agent
    
    print("✅ Successfully imported MAGI agent!")
    
    # Try creating an instance
    try:
        agent = create_magi_agent()
        print("✅ Successfully created MAGI agent instance!")
        print(f"Agent name: {agent.name}")
        print(f"Agent description: {agent.description}")
    except Exception as e:
        print(f"❌ Error creating MAGI agent: {e}")
        raise
        
except ImportError as e:
    print(f"❌ Failed to import MAGI agent: {e}")
    print("\nTroubleshooting steps:")
    print("1. Make sure you're in the project root directory")
    print("2. Check that MAGI/__init__.py exists and is properly configured")
    print("3. Verify that the MAGI directory is in your PYTHONPATH")
    print("4. Try running 'poetry install' again")
    raise
