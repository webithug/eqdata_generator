import click
import numpy as np


@click.command()
@click.option('--min', default=10,help='lower bound of the interval')
@click.option('--max', default=50,help='upper bound of the interval')
@click.option('--count',default=1000,help='number of counts')
@click.option('--dist',type=click.Choice(['uniform','gaus','poison'],case_sensitive=False))
def cli(min,max,count,dist):
    if dist=='uniform':
        click.echo(np.random.uniform(min,max,count))
    elif dist=='gaus':
        click.echo(np.random.normal((min+max)/2,min,count)) # mu, sigma, counts
    else:
        click.echo("I can only do uniform distribution lol")