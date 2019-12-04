	Summary:

This Python script uses a Monte Carlo simulation to obtain an exact
dose of medicine for a patient. It runs 10,000 trials at a time to
attempt to guess a winning sequence.


	To run:

To run, start in the directory with pill_dose_mc.py. From Python
prompt, issue commands:

from pill_dose_mc import *
meta_vial()

If one or more winning sequences are found, the final vial statuses
and the sequences are displayed.


	Problem description:

You have two vials. One vial is 3 mL, and one is 5 mL.

You have one water-soluble pill that is exactly one gram.

You have unlimited water.

The patient needs exactly 0.13 grams of medicine.

By dissolving the pill, filling the vials, pouring the water from one
vial to the other, and/or dumping water from vials, obtain the
required mass of medicine in one vial.

This problem was sourced from Dick Hess's book Mental Gymnastics.

The puzzle is called "You're the Doctor."
