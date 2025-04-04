import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def define_membership_functions():
    age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
    chol = ctrl.Antecedent(np.arange(100, 601, 1), 'chol')
    trestbps = ctrl.Antecedent(np.arange(80, 201, 1), 'trestbps')
    thalach = ctrl.Antecedent(np.arange(60, 211, 1), 'thalach')
    oldpeak = ctrl.Antecedent(np.arange(0, 7, 0.1), 'oldpeak')
    risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

    age.automf(3)
    chol.automf(3)
    trestbps.automf(3)
    thalach.automf(3)
    oldpeak.automf(3)

    risk['low'] = fuzz.trimf(risk.universe, [0, 0, 50])
    risk['medium'] = fuzz.trimf(risk.universe, [30, 50, 70])
    risk['high'] = fuzz.trimf(risk.universe, [50, 100, 100])

    return age, chol, trestbps, thalach, oldpeak, risk


def define_fuzzy_rules(age, chol, trestbps, thalach, oldpeak, risk):
    rule1 = ctrl.Rule(chol['poor'] & trestbps['poor'], risk['high'])
    rule2 = ctrl.Rule(age['good'] & thalach['good'], risk['low'])
    rule3 = ctrl.Rule(oldpeak['poor'], risk['high'])
    rule4 = ctrl.Rule(thalach['average'], risk['medium'])
    rule5 = ctrl.Rule(chol['average'] & trestbps['average'], risk['medium'])

    return [rule1, rule2, rule3, rule4, rule5]


def compute_risk(age_value, chol_value, trestbps_value, thalach_value, oldpeak_value):
    age, chol, trestbps, thalach, oldpeak, risk = define_membership_functions()
    rules = define_fuzzy_rules(age, chol, trestbps, thalach, oldpeak, risk)

    risk_ctrl = ctrl.ControlSystem(rules)
    risk_simulation = ctrl.ControlSystemSimulation(risk_ctrl)

    risk_simulation.input['age'] = age_value
    risk_simulation.input['chol'] = chol_value
    risk_simulation.input['trestbps'] = trestbps_value
    risk_simulation.input['thalach'] = thalach_value
    risk_simulation.input['oldpeak'] = oldpeak_value

    risk_simulation.compute()
    return risk_simulation.output['risk']