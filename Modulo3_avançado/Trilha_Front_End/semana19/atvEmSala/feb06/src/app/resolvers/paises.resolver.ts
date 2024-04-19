import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { GetPaisesService } from '../services/get-paises.service';
import { HttpClient } from '@angular/common/http';

export const paisesResolver: ResolveFn<string[]> = (route, state) => {
  
  let listaPaises = inject(GetPaisesService)

  return listaPaises.getPaises();
};
