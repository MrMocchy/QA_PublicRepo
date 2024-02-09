# cf: https://qiita.com/navitime_tech/items/a9ec5784901c7f8bfb57

from mine import *


Q = np.array([
	[-9, 4, 8],
	[0, -16, 16],
	[0, 0, -24]
	])


bqm = dimod.BinaryQuadraticModel(Q,offset=25, vartype=dimod.BINARY)

sampler = DWaveSampler(
	token=os.getenv("DWAVE_API_TOKEN"),
	solver = 'Advantage_system4.1'
	)
sampler = AutoEmbeddingComposite(sampler)

response = sampler.sample(bqm, num_reads=10)

# print(response)
# print(response.info)

[print(r) for r in response.record]

