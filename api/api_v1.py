from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from web.models import System, Variable


api = NinjaAPI(title='CKRETS API', version='0.8.1')

@api.get("/{system}")
def get_variables_by_system(request, system: str):
    system = get_object_or_404(System, acronym=system)
    variables = Variable.objects.filter(system_id=system.id)
    secrets_list = [{v.key : v.decrypted_value} for v in variables]
    return {'system': system.acronym, 'secrets': secrets_list}