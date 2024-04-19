import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProjectDetailComponent } from './components/project-detail/project-detail.component';


export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'project/:id', component: ProjectDetailComponent},

];
