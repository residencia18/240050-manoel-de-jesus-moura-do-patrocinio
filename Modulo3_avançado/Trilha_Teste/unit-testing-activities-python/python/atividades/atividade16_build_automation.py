from typing import List

# Simulando os modelos e enums
class StatusEnum:
    RUNNING = "RUNNING"

class InstallationEnum:
    INSTALLED = "INSTALLED"
    NOT_INSTALLED = "NOT_INSTALLED"

class AutomationModel:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

class RobotModel:
    def __init__(self, id, automation_id, installed):
        self.id = id
        self.automation_id = automation_id
        self.installed = installed

# Simulando a sessão do banco de dados
class db_context:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def query(self, model):
        # Método fictício para simular consultas ao banco de dados
        pass

# Simulando os métodos delay
def send_to_pack(robot_id):
    pass

def orchestration_create(automation_id):
    pass

def automation_build(automation_id: int):
    with db_context() as session:
        automation: AutomationModel | None = (
            session.query(AutomationModel).filter_by(id=automation_id).first()
        )
        robots: List[RobotModel | None] = (
            session.query(RobotModel)
            .filter_by(automation_id=automation.id)
            .all()
        )
        if len(robots) == 0: 
            return f'Automation {automation.name} has no robots to execute.'

        automation.status = StatusEnum.RUNNING.value
        session.commit()
        orchestration_valid = True
        for robot in robots:
            if robot.installed != InstallationEnum.INSTALLED.value:
                orchestration_valid = False
            if robot.installed == InstallationEnum.NOT_INSTALLED.value:
                send_to_pack(robot.id) # async call

        # if all robots are installed, create orchestration
        if orchestration_valid:
            orchestration_create(automation.id) # async call
            return f'Automation {automation.name} builded successfully'

        # retry automation build in 60 seconds
        automation_build(automation_id=automation.id) # async call
        return f'there is robots to install, building automation {automation.id} again'