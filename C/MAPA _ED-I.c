// A C program for Dijkstra's single source shortest path algorithm.
// The program is for adjacency matrix representation of the graph
  
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
  
// Number of vertices in the graph
#define V 5
  
// A utility function to find the vertex with minimum distance value, from
// the set of vertices not yet included in shortest path tree
int minDistance(int dist[], bool sptSet[])
{
    // Initialize min value
    int min = INT_MAX, min_index, v;
    for (v = 0; v < V; v++)
	{
        if (sptSet[v] == false && dist[v] <= min)
		{
            min = dist[v], min_index = v;
        }
	}    
    return min_index;
}
  
// A utility function to print the constructed distance array
void printSolution(int dist[])
{
    printf("\nVertex \t\t Distance from Source\n");
    int i;
    for (i = 0; i < V; i++)
	{
        printf("%d \t\t %d\n", i+1, dist[i]);
	}
}
  
// Function that implements Dijkstra's single source shortest path algorithm
// for a graph represented using adjacency matrix representation
void dijkstra(int graph[V][V], int src)
{
    int dist[V]; // The output array.  dist[i] will hold the shortest
    // distance from src to i
  
    bool sptSet[V]; // sptSet[i] will be true if vertex i is included in shortest
    // path tree or shortest distance from src to i is finalized
  
    // Initialize all distances as INFINITE and stpSet[] as false
    int i;
    for (i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
  
    // Distance of source vertex from itself is always 0
    dist[src] = 0;
  
    // Find shortest path for all vertices
    int count;
    for (count = 0; count < V-1; count++)
	{
        // Pick the minimum distance vertex from the set of vertices not
        // yet processed. u is always equal to src in the first iteration.
        int u = minDistance(dist, sptSet);
        
        // Mark the picked vertex as processed
        sptSet[u] = true;
  
        // Update dist value of the adjacent vertices of the picked vertex.
        int v;
        for (v = 0; v < V; v++)
		{
            // Update dist[v] only if is not in sptSet, there is an edge from
            // u to v, and total weight of path from src to  v through u is
            // smaller than current value of dist[v]
            if (!sptSet[v] && graph[u][v] != -1 && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
			{
                dist[v] = dist[u] + graph[u][v];
			}
		}
		printf("No da vez %d e a distancia e: %d\n", u+1, dist[u]);	
    }
  
    // print the constructed distance array
    //printSolution(dist);
}
  
// driver program to test above function
int main()
{
    /* Let us create the example graph discussed above */
    /* Sei que precisa ser assim: [(1-2)->200,(1-3)->0,(2-4)->0,(2-5)->100,(3-2)->900,(3-5)->600,(4-5)->200]*/
    int graph[V][V] ={	
 					{-1,200,0,-1,-1},
					{-1,-1,-1,0,100},
 					{-1,900,-1,-1,600},
 					{-1,-1,-1,-1,200},
 					{-1,-1,-1,-1,-1}
 					};
  
    dijkstra(graph, 0);
  
    return 0;
}
