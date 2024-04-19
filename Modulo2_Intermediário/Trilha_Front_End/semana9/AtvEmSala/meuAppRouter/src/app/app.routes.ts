import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ServicosComponent } from './components/servicos/servicos.component';
import { SobreComponent } from './components/sobre/sobre.component';

export const routes: Routes = [
    { 'path': '', component: HomeComponent },
    { 'path': 'servicos', component: ServicosComponent },
    { 'path': 'sobre', component: SobreComponent }
];
